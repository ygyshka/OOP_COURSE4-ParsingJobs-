from classes_dir.abc_class import ForJson
import json


class JsonWork(ForJson):
    """
    Класс для сохранения полученного списка в файл формата .json
    """

    JSON_PATH = 'data_json\list_vacancies.json'

    def save_vacancies(self, ending_data):
        """
        метод-класса для сохранения данных в файл
        :param ending_data:
        :return:
        """

        new_list = []
        for item in ending_data:
            new_list.append(item.__dict__)
        with open(JsonWork.JSON_PATH, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(new_list, indent=4, ensure_ascii=False))

    def show_vacancies(self):
        """
        метод-класса для чтения данных в файла
        :return:
        """

        with open(JsonWork.JSON_PATH, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data



