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
        pass

    def get_all_vacancies(self):
        """ Метод получает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию."""
        pass

    def get_avg_salary(self):
        """Метод получает среднюю зарплату по вакансиям. """
        pass

    def get_vacancies_with_higher_salary(self):
        """ Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. """
        pass

    def get_vacancies_with_keyword(self):
        """ Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова. """
        pass