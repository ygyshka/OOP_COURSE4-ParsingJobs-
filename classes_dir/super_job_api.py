from classes_dir.abc_class import ConnectorAPI
import requests


class SuperJobAPI(ConnectorAPI):
    """
    Класс для получения запроса к API сайта SuperJob
    """

    URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
    SUPER_JOB_API_KEY = 'v3.r.137692049' \
                        '.77fd46a2ace963e5d25728197d151e9375b8cc78' \
                        '.0f1c4701fe9bb8e1fb71c2bdc51e95c821d2651a'

    def get_request(self, vacancy):
        """
        Метод отрабатывает запрос пользователя и возвращает ответ API сайта
        :param vacancy:
        :return:
        """

        headers = {'X-Api-App-Id': SuperJobAPI.SUPER_JOB_API_KEY}
        params = {
            'keywords': vacancy,
            'page': 0,
            'count': 100,
        }
        response = requests.get(SuperJobAPI.URL_SJ, headers=headers, params=params)
        response.close()
        data_get = response.json()['objects']
        return data_get
