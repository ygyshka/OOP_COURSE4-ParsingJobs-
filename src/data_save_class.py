from src.abc_class import ForJson
import json


class JSONSaver(ForJson):

    JSON_PATH = '..\data_json\list_vacancies.json'

    def save_vacancies(self, ending_data):
        with open(JSONSaver.JSON_PATH, 'w', encoding='UTF-8') as f:
            json.dump(ending_data, f, indent=2, ensure_ascii=False)

    def show_vacancies(self):
        with open(JSONSaver.JSON_PATH, 'r', encoding='UTF-8') as f:
            file_content = f.read()
            get_data_json = json.loads(file_content)
        return get_data_json

    def delete_vacancies(self):
        pass

    def sorted_vacancies(self, text):
        pass

