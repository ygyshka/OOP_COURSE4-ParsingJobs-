from src.abc_class import ConnectorAPI
import requests


class HhAPI(ConnectorAPI):

    def __init__(self):
        self.req = None

    def get_request(self, vacancy):
        params = {
            'text': f'NAME:{vacancy}',  # Текст фильтра для подбора вакансий
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': 100  # Кол-во вакансий на 1 странице
        }
        self.req = requests.get('https://api.hh.ru/vacancies', params)
        self.req.close()
        res = self.req.json()['items']
        # all = []
        # for i in res:
        #     all.append(i["name"])
        return res

if __name__ == '__main__':
    emp1 = HhAPI()
    print(emp1.get_request('Аналитик')) #-------- #нужно
