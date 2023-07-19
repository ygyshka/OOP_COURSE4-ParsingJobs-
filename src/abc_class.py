from abc import ABC, abstractmethod


class ConnectorAPI(ABC):
    @abstractmethod
    def get_connect(self):
        pass

    @abstractmethod
    def get_vacancies(self):
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
