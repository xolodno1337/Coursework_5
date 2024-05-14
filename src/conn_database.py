import psycopg2


with psycopg2.connect(
        host='localhost',
        database='Vacancies_hh',
        user='postgres',
        password='7856'
) as conn:
    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancy_hh (
                    name_company varchar (100),
                    title varchar(100),
                    url_vacancy varchar(100),
                    salary_from int,
                    salary_to int,
                    description text,
                    requirement text); 
                    """)
