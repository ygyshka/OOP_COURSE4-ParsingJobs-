from classes_dir.hh_api import HhAPI
from classes_dir.data_save_class import JsonWork
from classes_dir.super_job_api import SuperJobAPI
from src.func import get_vacancies_hh, get_vacancies_sj, \
    get_vacancies_by_salary, show_vacancies, get_vacancy_from_file, get_top_by_salary, search_by_words


def user_instruction():
    """
    Фенкция отработки сценария пользователя(читать README.md).
    :return:
    """
    hh_response = HhAPI()
    sj_response = SuperJobAPI()
    json_save = JsonWork()
    json_read = JsonWork()

    user_search = input('Введите запрос для поиска вакансий на платформах HeadHunter и SuperJob:\n')
    while True:
        list_1 = get_vacancies_hh(hh_response.get_request(user_search.lower()))
        list_2 = get_vacancies_sj(sj_response.get_request(user_search.lower()))
        list_1.extend(list_2)
        if len(list_1) == 0:
            print('Вакансии не найдены!')

            break

        operations_ = ['1: Вывод вакансии по ключевым словам.',
                       '2: Вывести топ N вакансий по зарплате.',
                       '3: Вывести вакансии по минимальному погору зарплаты.',
                       '4: Вывести полный список вакансий',
                       'Enter "Stop" to exit.']

        for v in operations_:
            print(v)
        operation_number = input("Выбирете операцию для обработки запроса\n")

        if operation_number == '1':
            json_save.save_vacancies(list_1)

            using_list = get_vacancy_from_file(
                json_read.show_vacancies())  # --------- Вывод вакансий по ключевым словам
            words = str(input('Введите ключевые слова для фильтрации вакансий:\n')).lower()
            show_vacancies(search_by_words(using_list, words))
            continue__ = input('Хотите повторить запрос?\n'
                               '(да/нет):')
            if continue__ == "да":
                continue
            else:
                break
        elif operation_number == '2':
            json_save.save_vacancies(list_1)

            using_list = get_vacancy_from_file(json_read.show_vacancies())
            choise = int(input('Введите количество вакансий для вывода в топ N по зарплате:\n'))
            show_vacancies(get_top_by_salary(using_list, choise))
            continue__ = input('Хотите повторить запрос?\n'
                               '(да/нет):')
            if continue__ == "да":
                continue
            else:
                break
        elif operation_number == '3':
            json_save.save_vacancies(list_1)

            using_list = get_vacancy_from_file(json_read.show_vacancies())
            choise = input('Введите минимальный парог зарплаты:\n')
            show_vacancies(get_vacancies_by_salary(using_list, choise))
            continue__ = input('Хотите повторить запрос?\n'
                               '(да/нет):')
            if continue__ == "да":
                continue
            else:
                break
        elif operation_number == '4':
            json_save.save_vacancies(list_1)

            using_list = get_vacancy_from_file(json_read.show_vacancies())
            show_vacancies(using_list)
            continue__ = input('Хотите повторить запрос?\n'
                               '(да/нет):')
            if str(continue__) == "да":
                continue
            else:
                break
        elif operation_number == "Stop":
            print("Спасибо что воспользовались программой!")
            break


if __name__ == '__main__':
    user_instruction()
