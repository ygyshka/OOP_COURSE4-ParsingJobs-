import json
from src.abc_class import VacAll
from src.hh_api import HhAPI
from src.data_save_class import JSONSaver
from src.super_job_api import SuperJobAPI


class VacanciesHH(VacAll):

    def __init__(self, data, ):
        self.name = data['name']
        self.url_vac = data['alternate_url']
        self.salary, self.midl_salary = VacanciesHH.get_salary(self, data)
        self.description = data['snippet']['responsibility']

    def get_salary(self, data):

        if data['salary'] is None:
            self.salary = "Зарплата по результатам собеседования"
            self.midl_salary = 0
            return self.salary, self.midl_salary
        elif data['salary']['from'] != None and data['salary']['to'] == None:
            self.salary = data['salary']['from']
            self.midl_salary = self.salary
            return f'Зарплата {self.salary}', self.midl_salary
        elif data['salary']['from'] == None and data['salary']['to'] != None:
            self.salary = data['salary']['to']
            self.midl_salary = self.salary
            return f'Зарплата {self.salary}', self.midl_salary
        else:
            self.salary = f'Зарплата от {data["salary"]["from"]} до {data["salary"]["to"]}'
            self.midl_salary = (data["salary"]["from"] + data["salary"]["to"]) / 2
        return f'Зарплата {self.salary}', self.midl_salary

    def __repr__(self):
        return f'---{self.name}---\n---{self.description}---\n---{self.url_vac}---\n---{self.salary}\n'

    def get_view_to_save(self):
        data_json = {'name': self.name,
                     'description': self.description,
                     'salary': self.salary,
                     'url': self.url_vac,
                     'midl_salary': self.midl_salary
                     }

        return data_json

    @classmethod
    def another_vacancies_place(cls, other_data):
        pass


class VacanciesSJ(VacAll):

    def __init__(self, data):

        self.name = data['profession']
        self.url_vac = data['link']
        self.salary = VacanciesSJ.get_salary(self, data)
        self.description = data['candidat']

    def get_salary(self, data):
        if data["payment_from"] and data["payment_to"]:
            self.salary = f'Зарплата от {data["payment_from"]} до {data["payment_to"]}'
            return self.salary
        elif data["payment_to"] == 0 and data["payment_from"] != 0:
            self.salary = data["payment_from"]
            return f'Зарплата {self.salary}'
        elif data["payment_to"] != 0 and data["payment_from"] == 0:
            self.salary = data["payment_to"]
            return f'Зарплата {self.salary}'
        else:
            self.salary = 'Зарплата по результатам собеседования'
            return self.salary

    def __repr__(self):
        return f'---{self.name}---\n---{self.description}---\n---{self.url_vac}---\n---{self.salary}\n'

    def get_view_to_save(self):
        data_json = {'name': self.name,
                     'description': self.description,
                     'salary': self.salary,
                     'url': self.url_vac}
        return data_json


if __name__ == '__main__':
    #### Пример для хх
    # emp1 = HhAPI()
    # lol = emp1.get_request("Аналитик")
    # show = [VacanciesHH(emp) for emp in lol]
    # save_data = []
    # for sh in show:
    #     #print(sh.salary)
    #     save_data.append(sh.get_view_to_save())
    #
    # save_json = JSONSaver()
    # save_json.save_vacancies(save_data)
    #
    # with open(JSONSaver.JSON_PATH, 'r', encoding='UTF-8') as f:
    #     file_content = f.read()
    #     get_data_json = json.loads(file_content)
    # for item in get_data_json:
    #     for k, v in item.items():
    #         print(v)

    ### Пример для суперджоба
    emp = SuperJobAPI()
    lol = emp.get_request("Аналитик")
    show = [VacanciesSJ(emp) for emp in lol]
    save_data = []
    for sh in show:
        save_data.append(sh.get_view_to_save())

    save_json = JSONSaver()
    save_json.save_vacancies(save_data)

    show_data_ = JSONSaver()
    gt = show_data_.show_vacancies()
    rep = 0
    for item in gt:
        # print(item['salary'])
        while rep < 10:
            for k, v in item.items():
                print(k)
                print(v)

            rep += 1
    print(type(gt))
