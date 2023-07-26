from src.abc_class import ConnectorAPI
import requests


class SuperJobAPI(ConnectorAPI):
    # а  в суперджобе  получай по  ключу['objects'], тоже будет список словарей

    URL_SJ = 'https://api.superjob.ru/2.0/vacancies/'
    SUPER_JOB_API_KEY = 'v3.r.137692049' \
                        '.77fd46a2ace963e5d25728197d151e9375b8cc78' \
                        '.0f1c4701fe9bb8e1fb71c2bdc51e95c821d2651a'

    def __init__(self):
        self.response = None

    def get_request(self, vacancy):

        headers = {'X-Api-App-Id': SuperJobAPI.SUPER_JOB_API_KEY}
        params = {
            'keywords': vacancy,
            'page': 0,
            'count': 100,
        }
        self.response = requests.get(SuperJobAPI.URL_SJ, headers=headers, params=params)
        self.response.close()
        res = self.response.json()['objects']
        # self.response.close()
        # res = self.response.json()#['objects']
        # all = []
        # for i in res:
        #     all.append(i["name"])
        # return all

        return res

if __name__ == '__main__':
    emp = SuperJobAPI()
    print(emp.get_request('Аналитик'))
    # for it in emp.get_request('Аналитик'):
    #     print(f'{it}\n')
