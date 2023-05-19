from src.data_processing_classes import FileHandling
from src.get_preparation_classes import HHGetVacansies, SJGetVacansies


def any_key():
    return f'Любое другое значение (или просто Enter) - '


def chose_vacancy():
    vacansy = input(f'Введите ключевое слово для поиска вакансии: ').lower()
    return vacansy


def start_parsing(vacansy):
    """Старт парсинга. Выбор пользователем порталов используемых для поиска"""

    choise = input(f'Для поиска вакансий введите одно из значений:\n'
                   f'1 - поиск только на сайте HeadHanter\n'
                   f'2 - поиск только на сайте SuperJob\n'    
                   f'{any_key()}поиск на обоих сайтах\n'
                   f'Ваш выбор: '
                   )

    if choise == '1':
        hh = HHGetVacansies(vacansy)
        converted_vacansies = hh.validate_vacansies()
    elif choise == '2':
        sj = SJGetVacansies(vacansy)
        converted_vacansies = sj.validate_vacansies()
    else:
        hh = HHGetVacansies(vacansy)
        sj = SJGetVacansies(vacansy)
        converted_vacansies = hh.validate_vacansies()
        converted_vacansies.extend(sj.validate_vacansies())

    return converted_vacansies


def main():
    print("Здравствуйте!")
    vacansy = chose_vacancy()
    converted_vacansies = start_parsing(vacansy)
    print(f'Найдено результатов: {len(converted_vacansies)}\n\n')

    fh = FileHandling(vacansy, converted_vacansies)

    choise_filtred = input(f'Вы можете фильтровать вакансии, выбрав одно из значений:\n'
                           f'1 - по городу\n'
                           f'2 - по работодателю\n'
                           f'{any_key()}не фильтровать\n'
                           f'Ваш выбор: '
                           )

    if choise_filtred == '1':
        filter_field = 'area'
        filter_value = input('Введите название города: ').lower()
        vacansies = fh.filtred_vacansies(filter_field, filter_value)
    elif choise_filtred == '2':
        filter_field = 'employer'
        filter_value = input('Введите название работодателя: ').lower()
        vacansies = fh.filtred_vacansies(filter_field, filter_value)
    else:
        vacansies = fh.not_filtred_vacansies()

    choise_sorted = input(f'Вы можете сортировать вакансии, выбрав одно из значений:\n'
                          f'1 - по минимальной зарплате по убыванию\n'
                          f'2 - по максимальной зарплате по убыванию\n'
                          f'{any_key()}не сортировать')

    if choise_sorted == '1':
        vacansies = sorted(vacansies, reverse=True)
    elif choise_sorted == '2':
        vacansies = sorted(vacansies, key=lambda x: x.salary_to if x.salary_to else 0, reverse=True)

    for vacans in vacansies:
        print(vacans, end='\n\n')

    print(f'Подобрано вакансий: {len(vacansies)}')


if __name__ == '__main__':
    main()
    