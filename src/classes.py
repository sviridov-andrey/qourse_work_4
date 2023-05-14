from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):

    @abstractmethod
    def get_response(self):
        pass

    @abstractmethod
    def get_vacansies(self):
        pass


class HHGetVacansies(AbstractAPI):
    """Получает инфорацию API о вакансиях с сайта HH"""

    def __init__(self, vacansy):
        self.__param = {
            "text": vacansy,
            "page": 0,
            "per_page": 100
        }
        self.__vacansies = []

    def get_response(self):
        """Парсинг одной страницы с вакансиями"""

        response = requests.get("https://api.hh.ru/vacancies", self.__param)
        if response.status_code == 200:
            return response.json()['items']
        else:
            print(f'Страница {self.__param["page"]+1}  ошибка получения данных {response.status_code}')

    def get_vacansies(self):
        pass


    # def __str__(self):
    #     return f'{self.vacancy_list}'


a = HHGetVacansies('python')
#a.ggg()

print(a.get_response())
# print(len(a['items']))
