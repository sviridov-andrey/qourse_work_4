from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacansys(self):
        pass


class HHGetVacansys(AbstractAPI):
    __hh_url: str = 'https://api.hh.ru/'

    @classmethod
    def get_vacansys(cls, vacansy):
        response = requests.get(cls.__hh_url + "vacancies", params={"text": vacansy})
        vacancy_list = response.json()
        return vacancy_list

    def __str__(self):
        return f'{self.vacancy_list}'


a = HHGetVacansys.get_vacansys('python')
print(a)