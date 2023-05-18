import json

from src.get_preparation_classes import SJGetVacansies, HHGetVacansies
from src.abstract_classes import AbstractJson


class FileHandling(AbstractJson):
    """Обработка файла со списком вакансий"""
    def __init__(self, vacansy, all_vacansies):
        self.__filename = f'{vacansy.title()}.json'
        self.all_vacansies = all_vacansies

    def create_file(self):
        """Запись в файл списка вакансий"""
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(self.all_vacansies)


    def load_file(self):
        """Загрузка из файла списка вакансий"""
        pass
    pass


class Vacansy:
    def __init__(self):
        pass


a = SJGetVacansies('менеджер')
v = a.validate_vacansies()
for i in v:
    print(i)
