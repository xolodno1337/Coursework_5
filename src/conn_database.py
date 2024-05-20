import json
import psycopg2


def connection():
    # Создаем базу данных
    try:
        conn = psycopg2.connect(user="postgres", password=7856)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute("CREATE DATABASE vacancies_hh")
        conn.close()
    except:
        pass

    #   Создаем таблицу в базе данных
    with psycopg2.connect(
            host='localhost',
            database='vacancies_hh',
            user='postgres',
            password='7856'
    ) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    CREATE TABLE vacancy_hh (
                        company varchar (100),
                        title varchar(100),
                        url_vacancy varchar(100),
                        salary_from int,
                        salary_to int,
                        description text,
                        requirement text);
                        """)
            except:
                pass
    #   Заполняем таблицы в базе данных
    with psycopg2.connect(
            host='localhost',
            database='vacancies_hh',
            user='postgres',
            password='7856'
    ) as conn:
        with conn.cursor() as cur:
            try:
                with open('vacancy.json', 'r', encoding='utf-8') as file:
                    vacancies = json.load(file)
                    for vacancy in vacancies:
                        cur.execute(
                            'INSERT INTO vacancy_hh (company, title, url_vacancy, salary_from, salary_to, '
                            'description, requirement) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                            (vacancy.get('company'), vacancy.get('title'), vacancy.get('url_vacancy'),
                             vacancy.get('salary_from'), vacancy.get('salary_to'), vacancy.get('description'),
                             vacancy.get('requirement')))
            except:
                pass
