import json
#from classes_dir.abc_class import VacAll
from classes_dir.hh_api import HhAPI
#from classes_dir.data_save_class import JSONSaver
from classes_dir.super_job_api import SuperJobAPI


class Vacancies:
    """
    Класс получения экзепляров списка вакансий для дальнейшей обработки данных
    """

    def __init__(self, web_id, name, city, url, salary_from, salary_to, currency, description):
        self.web_id = web_id
        self.name = name
        self.city = city
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.salary_mean = Vacancies.get_salary_mean(self)

    def get_salary_mean(self):
        """
        Метод получения атрибута экземпляра для фильтрации списка экземпляров
        :return:
        """

        if self.salary_to != 0 and self.salary_to is not None:
            self.salary_mean = self.salary_to
        else:
            self.salary_mean = 0
        return self.salary_mean

    def __repr__(self):
        return f'Vacancy(vacancy_id={self.web_id},' \
               f'name={self.name} ' \
               f'city={self.city},' \
               f'url={self.url}, ' \
               f'salary={self.salary_from}-{self.salary_to},' \
               f'currency={self.currency},' \
               f'description={self.description})'

    def __str__(self):
        salary = ''
        if self.salary_from and self.salary_to:
            salary = f'Зарплата: от {self.salary_from} {self.currency}. до {self.salary_to} {self.currency}.'
        if (self.salary_from == 0 or self.salary_from is None) and (self.salary_to == 0 or self.salary_to is None):
            salary = f'Зарплата по результатам собеседования !'
        elif self.salary_to == 0 or self.salary_to is None:
            salary = f'Зарплата: от {self.salary_from} {self.currency}.'
        elif self.salary_from == 0 or self.salary_from is None:
            salary = f'Зарплата: от {self.salary_to} {self.currency}.'

        return f'web_id: {self.web_id}\n' \
               f'Профессия: {self.name}\n' \
               f'Место работы: {self.city}\n' \
               f'Ссылка на вакансию: {self.url}\n' \
               f'{salary}\n' \
               f'Описание:\n{self.description}\n'

    def __gt__(self, other):
        return self.salary_mean > other.salary_mean
