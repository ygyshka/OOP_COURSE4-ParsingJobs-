from abc import ABC, abstractmethod


class VacAll(ABC):
    def get_salary(self, data):
        pass

    def get_view_to_save(self):
        pass


class ConnectorAPI(ABC):
    @abstractmethod
    def get_request(self, vacancy):
        pass


class ForJson(ABC):

    def save_vacancies(self, response_api):
        pass

    def show_vacancies(self):
        pass

    def delete_vacancies(self):
        pass

    def sorted_vacancies(self, text):
        pass
