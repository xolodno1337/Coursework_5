from src.DBManager import DBManager
from src.conn_database import connection
from src.func import get_company, save_vacancy


def main():
    new = DBManager('localhost', 'vacancies_hh', 'postgres', 7856)
    print(f'''Что вы хотите увидеть?:
          1 - Посмотреть список всех компаний и количество вакансий у каждой компании;
          2 - Посмотреть список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию;
          3 - Посмотреть среднюю зарплату по всем вакансиям;
          4 - Посмотреть список всех вакансий, у которых зарплата выше средней по всем вакансиям;
          5 - Посмотреть список всех вакансий, в названии которых содержатся запрашиваемое слово.''')
    user_input = input('Введите цифру: ')
    if user_input == '1':
        for i in new.get_companies_and_vacancies_count():
            print(f'Компания:{i[0]}, Количество вакансий:{i[1]}')
    if user_input == '2':
        for i in new.get_all_vacancies():
            print(f'Компания:{i[0]}, Вакансия:{i[1]}, Зарплата от {i[2]} до {i[3]}, Ссылка:{i[4]}')
    elif user_input == '3':
        for i in new.get_avg_salary():
            print(f'Средняя зарплата по всем вакансиям: {i[0]}')
    elif user_input == '4':
        for i in new.get_vacancies_with_higher_salary():
            print(f'Вакансия: {i[0]}, Зарплата от {i[1]}')
    elif user_input == '5':
        keyword = input('По какому слову будем искать?: ')
        for i in new.get_vacancies_with_keyword(keyword):
            print(i)
    else:
        print('Некорректный ввод')


main()
