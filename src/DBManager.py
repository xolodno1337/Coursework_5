import psycopg2


class DBManager:
    """ Класс, который будет подключаться к БД PostgreSQL. """

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password, )
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """ Метод получает список всех компаний и количество вакансий у каждой компании. """
        self.cur.execute("""SELECT company, COUNT (*) FROM vacancy_hh GROUP BY company""")
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """ Метод получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию."""
        self.cur.execute("""SELECT company, title, salary_from, salary_to, url_vacancy FROM vacancy_hh""")
        return self.cur.fetchall()

    def get_avg_salary(self):
        """Метод получает среднюю зарплату по вакансиям. """
        self.cur.execute("""SELECT AVG(salary_from) FROM vacancy_hh""")
        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """ Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. """
        self.cur.execute("""SELECT title, salary_from FROM vacancy_hh WHERE salary_from > (SELECT AVG(salary_from) 
        FROM vacancy_hh)""")
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """ Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова. """
        query = """
                SELECT * FROM vacancy_hh
                WHERE LOWER(title) LIKE %s
                """
        self.cur.execute(query, ('%' + keyword.lower() + '%',))
        return self.cur.fetchall()