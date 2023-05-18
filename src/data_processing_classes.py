import json

from src.get_preparation_classes import SJGetVacansies, HHGetVacansies
from src.abstract_classes import AbstractJson


class FileHandling(AbstractJson):
    """Обработка файла со списком вакансий"""
    def __init__(self, vacansy, all_vacansies):
        self.__filename = f'{vacansy.title()}.json'
        self.all_vacansies = all_vacansies
        self.create_file()
        print("Инициализация")

    def create_file(self):
        """Запись в файл списка вакансий"""

        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(self.all_vacansies, file, ensure_ascii=False, indent=4)

    def load_file(self):
        """Загрузка из файла списка вакансий"""
        pass


class Vacansy:
    __slots__ = ("title", "employer", "url", "area", "experience", "employment", "salary",
                 "salary_from", "salary_to", "currency", "portal")

    def __init__(self, title, employer, url, area, experience, employment, salary,
                 salary_from, salary_to, currency, portal):
        self.title = title
        self.employer = employer
        self.url = url
        self.area = area
        self.experience = experience
        self.employment = employment
        self.salary = salary
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.portal = portal

    def __gt__(self, other):
        if not other.salary_from:
            return True
        elif not self.salary_from:
            return False
        return self.salary_from >= other.salary_from

    def __str__(self):
        if self.salary is False:
            salary_from = 'не указана'
            salary_to = ''
            currency = ''

        else:
            currency = self.currency
            if self.salary_from or self.salary_from != 0:
                salary_from = f'От {self.salary_from}'
            else:
                salary_from = f''
            if self.salary_to or self.salary_to != 0:
                salary_to = f'От {self.salary_to}'
            else:
                salary_to = f''

        return f'Вакансия: {self.title}\nРаботодатель: {self.employer}\nГород: {self.area}\nURL: {self.url}\n' \
               f'Зарплата: {salary_from} {salary_to} {currency}\nОпыт: {self.experience}\n' \
               f'Занятость: {self.employment}\nВакансия с сайта: {self.portal}'

