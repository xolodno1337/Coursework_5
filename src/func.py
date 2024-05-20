import json
import requests


def get_company():
    """ Функция, которая получает вакансии и добавляет в новый список нужные данные. """
    vacancies = []
    companies = [
        "АО Лада-Имидж",  # 41004
        "Яндекс",  # 1740
        "PepsiCo",  # 581458
        "Тинькофф",  # 78638
        "VK",  # 15478
        "Ozon",  # 2180
        "Sber",  # 3529
        "Циан",  # 1429999
        "ПАО Газпром нефть",  # 39305
        "Лукойл"  # 907345
    ]
    for i in companies:
        url = "https://api.hh.ru/vacancies"
        params = {'text': i, 'per_page': 100}
        data = requests.get(url, params=params)

        for item in data.json()['items']:
            title = item['name']
            url_vacancy = item['alternate_url']
            salary = item['salary']
            if salary:
                salary_from = salary.get('from')
                salary_to = salary.get('to')
            description = item['snippet']['responsibility']
            requirement = item['snippet']['requirement']

            vacancies.append({
                "company": i,
                "title": title,
                "url_vacancy": url_vacancy,
                "salary_from": salary_from,
                "salary_to": salary_to,
                "description": description,
                "requirement": requirement
            })
    return vacancies


def save_vacancy():
    """ Функция сохраняет полученные вакансии в формате json. """
    vacancies = get_company()
    for vacancy in vacancies:
        print(vacancy)
        filename = 'vacancy.json'
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(vacancies, outfile, ensure_ascii=False, indent=4)
