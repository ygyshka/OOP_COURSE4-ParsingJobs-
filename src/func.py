import operator
from classes_dir.vacancy_info import Vacancies


def get_vacancies_hh(data):
    """
    Функция конвертации полученного ответа с сайта HeadHanter
    :param data:
    :return:
    """

    list_vac = []
    for item in data:
        vacancy = Vacancies(item['id'], item['name'], item['area']['name'],
                            item['alternate_url'], item['salary']['from'],
                            item['salary']['to'], item["salary"]["currency"],
                            item['snippet']['responsibility'])
        list_vac.append(vacancy)
    return list_vac


def get_vacancies_sj(data):
    """
    Функция конвертации полученного ответа с сайта SuperJob
    :param data:
    :return:
    """

    list_vac = []
    for item in data:
        vacancy = Vacancies(item['id'], item["profession"], item["town"]["title"],
                            item['link'], item['payment_from'],
                            item['payment_to'], item["currency"],
                            item['vacancyRichText'])
        list_vac.append(vacancy)
    return list_vac


def get_vacancy_from_file(data):
    """
    Функция конвертации списка вакансий из файла .json
    :param data:
    :return:
    """

    list_vac = []
    for item in data:
        vacancy = Vacancies(item['web_id'], item["name"], item["city"],
                            item['url'], item['salary_from'], item['salary_to'],
                            item["currency"], item['description'])
        list_vac.append(vacancy)
    return list_vac


def show_vacancies(data):
    """
    Функция отображения данных пользователю
    :param data:
    :return:
    """

    for item in data:
        print(item)
    print(f'По вашему запросу найденно {len(data)} результата(-ов)!\n'
          f'Для просмотра результатов листайте вверх\n')


def search_by_words(data, word):
    """
    Функция поиска вакансий по ключевым словам(запросу пользователя)
    :param data:
    :param word:
    :return:
    """

    work_list = []
    exit_list = []
    list_by_words = []
    for i in data:
        work_list.append(i.__dict__)
    for item in work_list:
        vac = Vacancies(item['web_id'], item["name"], item["city"],
                        item['url'], item['salary_from'], item['salary_to'],
                        item["currency"], item['description'])
        list_by_words.append(vac)
    for value in list_by_words:
        if word.lower() in value.name.lower():
            exit_list.append(value)
        else:
            continue
    return exit_list


def get_top_by_salary(data, num):
    """
    Функция фильтрации списка в вормате - "топ N по зарплате"
    :param data:
    :param num:
    :return:
    """

    new_list = []
    n1 = []
    for i in data:
        new_list.append(i.__dict__)
    sorted_list = sorted(new_list, key=operator.itemgetter('salary_mean'), reverse=True)
    for item in sorted_list[:num]:
        emp = Vacancies(item['web_id'], item["name"], item["city"],
                        item['url'], item['salary_from'], item['salary_to'],
                        item["currency"], item['description'])
        n1.append(emp)
    return n1


def get_vacancies_by_salary(data, numb):
    """
    Функция фильтрации списка вакансий не ниже указаной зарплаты
    :param data:
    :param numb:
    :return:
    """

    new_list = []
    for item in data:
        if item.salary_from is None:
            continue
        if item.currency == "RUR" or item.currency == "rub":
            if int(numb) <= int(item.salary_from):
                new_list.append(item)
    return new_list
