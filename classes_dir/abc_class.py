from abc import ABC, abstractmethod


class ConnectorAPI(ABC):
    """
    Абстрактный класс для классов получения API
    """
    @abstractmethod
    def get_request(self, vacancy):
        pass


class ForJson(ABC):
    """
    Абстрактный класс для класса сохранения данных в файл
    """

    def save_vacancies(self, response_api):
        pass

    def show_vacancies(self):
        pass

