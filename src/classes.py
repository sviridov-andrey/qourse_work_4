import os
import requests
from src.abstract_classes import AbstractAPI


class HHGetVacansies(AbstractAPI):
    """Получает инфорацию API о вакансиях с сайта HH"""

    def __init__(self, vacansy: str):
        self.vacansy = vacansy
        self.vacansies = []
        self.__api_str = "https://api.hh.ru/vacancies"
        self.__first_key = 'items'
        self.__header = ''
        self.__param = {
            "text": self.vacansy,
            "page": 0,
            "per_page": 100
        }

    @property
    def get_api_str(self):
        return self.__api_str

    @property
    def get_first_key(self):
        return self.__first_key

    @property
    def get_header(self):
        return self.__header

    @property
    def get_param(self):
        return self.__param

    def get_response(self):
        """Парсинг одной страницы с вакансиями"""

        response = requests.get(self.get_api_str,
                                headers=self.get_header, params=self.get_param)
        if response.status_code == 200:
            return response.json()[self.get_first_key]

    def get_vacansies(self, count_page=10):
        """Получение списка вакансий"""

        while self.__param['page'] < count_page:
            one_page_vacansies = self.get_response()
            if one_page_vacansies is not None:
                self.vacansies.extend(one_page_vacansies)
                self.__param['page'] += 1
            else:
                print(f'Страница {self.__param["page"] + 1} ошибка получения данных')
                break

        return self.vacansies

    def validate_vacansies(self):
        """Валидация списка вакансий с фильтрацией вакансий не входящих в запрос"""

        self.get_vacansies()
        converted_vacansies = []
        for vac in self.vacansies:
            if self.vacansy in vac['name'].lower():
                if vac.get('salary') is not None:
                    salary = {'salary': True,
                              'salary from': vac['salary']['from'],
                              'salary to': vac['salary']['to'],
                              'currency': vac['salary']['currency']
                              }
                else:
                    salary = {'salary': False,
                              'salary from': None,
                              'salary to': None,
                              'currency': None
                              }
                vacansy_params = {'id': vac['id'],
                                  'title': vac['name'],
                                  'employer': vac['employer']['name'],
                                  'url': vac['alternate_url'],
                                  'area': vac['area']['name'],
                                  'experience': vac['experience']['name'],
                                  'employment': vac['employment']['name'],
                                  'portal': 'HeadHunter'
                                  }
                vacansy_params.update(salary)
                converted_vacansies.append(vacansy_params)

        return converted_vacansies


class SJGetVacansies(HHGetVacansies):
    """Получает инфорацию API о вакансиях с сайта SuperJob"""

    def __init__(self, vacansy: str):
        super().__init__(vacansy)
        self.vacansy = vacansy
        self.__vacansies = []
        self.__api_str = "https://api.superjob.ru/2.0/vacancies"
        self.__first_key = "objects"
        self.__header = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}
        self.__param = {
            "keyword": self.vacansy,
            "page": 0,
            "count": 100
        }

    @property
    def get_api_str(self):
        return self.__api_str

    @property
    def get_first_key(self):
        return self.__first_key

    @property
    def get_header(self):
        return self.__header

    @property
    def get_param(self):
        return self.__param

    def validate_vacansies(self):
        """Валидация списка вакансий с фильтрацией вакансий не входящих в запрос"""

        self.get_vacansies()
        converted_vacansies = []
        for vac in self.vacansies:
            if self.vacansy in vac['profession'].lower():
                if vac['payment_from'] == 0 and vac['payment_to'] == 0:
                    salary = {'salary': False,
                              'salary from': vac['payment_from'],
                              'salary to': vac['payment_to'],
                              'currency': vac['currency']
                              }
                else:
                    salary = {'salary': True,
                              'salary from': vac['payment_from'],
                              'salary to': vac['payment_to'],
                              'currency': vac['currency']
                              }
                vacansy_params = {'id': vac['id'],
                                  'title': vac['profession'],
                                  'employer': vac['firm_name'],
                                  'url': vac['link'],
                                  'area': vac['town']['title'],
                                  'experience': vac['experience']['title'],
                                  'employment': vac['type_of_work']['title'],
                                  'portal': 'SuperJob'
                                  }
                vacansy_params.update(salary)
                converted_vacansies.append(vacansy_params)

        return converted_vacansies


class FileHandling:
    """Обработка файла со списком вакансий"""
    def __init__(self, vacansy):
        self.__filename = vacansy

    def create_file(self):
        """Запись в файл списка вакансий"""
        with open(self.__filename, 'w', encoding='utf-8') as file:


    def load_file(self):
        """Загрузка из файла списка вакансий"""
        pass
    pass


class Vacansy:
    def __init__(self):
        pass


a = HHGetVacansies('менеджер')
v = a.validate_vacansies()
for i in v:
    print(i)

