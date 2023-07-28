from classes_dir.abc_class import ConnectorAPI
import requests


class HhAPI(ConnectorAPI):
    """
    Класс для получения запроса к API сайта HeadHunter
    """

    URl_HH = 'https://api.hh.ru/vacancies'

    def get_request(self, vacancy):
        """
        Метод отрабатывает запрос пользователя и возвращает ответ API сайта
        :param vacancy:
        :return:
        """

        params = {
            'text': f'NAME:{vacancy}',  # Текст фильтра для подбора вакансий
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100,  # Кол-во вакансий на 1 странице
            'only_with_salary': True
        }
        response = requests.get(HhAPI.URl_HH, params)
        response.close()
        data_get = response.json()['items']
        return data_get

