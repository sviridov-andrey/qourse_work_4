from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):

    @abstractmethod
    def get_response(self):
        pass

    @abstractmethod
    def get_vacansies(self):
        pass

    @abstractmethod
    def validate_vacansies(self):
        pass


class HHGetVacansies(AbstractAPI):
    """Получает инфорацию API о вакансиях с сайта HH"""

    def __init__(self, vacansy):
        self.vacansy = vacansy
        self.__param = {
            "text": self.vacansy,
            "page": 0,
            "per_page": 100
        }
        self.__vacansies = []

    def get_response(self):
        """Парсинг одной страницы с вакансиями"""

        response = requests.get("https://api.hh.ru/vacancies", self.__param)
        if response.status_code == 200:
            return response.json()['items']

    def get_vacansies(self, count_page=10):
        """Получение списка вакансий"""

        while self.__param['page'] < count_page:
            one_page_vacansies = self.get_response()
            if one_page_vacansies is not None:
                self.__vacansies.extend(one_page_vacansies)
                self.__param['page'] += 1
            else:
                print(f'Страница {self.__param["page"] + 1} ошибка получения данных')
                break

        return self.__vacansies

    def validate_vacansies(self):
        """Валидация списка вакансий с отсеиванием вакансий не входящих в запрос"""

        converted_vacansies = []
        for vac in self.__vacansies:
            if self.vacansy in vac['name'].lower():
                converted_vacansies.append({
                    'id': vac['id'],
                    'title': vac['name'],
                    'employer': vac['employer']['name'],
                    'url': vac['alternate_url'],
                    'salary from': vac['salary']['from'],
                    'salary to': vac['salary']['to'],
                    'currency': vac['salary']['currency'],
                    'area': vac['area']['name'],
                    'experience': vac['experience']['name'],
                    'employment': vac['employment']['name']
                })

        return converted_vacansies



    # def __repr__(self):
    #     return self.__vacansies


a = HHGetVacansies('тестировщик')
vac = []
for i in a.get_vacansies():
    if 'тестировщик' in i['name'].lower():  # and 'python' in i:
        print(i)
        break

print(len(vac))
print(*vac, sep='\n')
# print(len(a['items']))
