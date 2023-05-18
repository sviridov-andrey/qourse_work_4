from src.get_preparation_classes import HHGetVacansies, SJGetVacansies


def any_key():
    return f'Любое другое значение (или просто Enter) - '


def chose_vacancy():
    # vacansy = input(f'Введите ключевое слово для поиска вакансии: ').lower()
    vacansy = 'менеджер'
    return vacansy


def start_parsing(vacansy):
    """Старт парсинга. Выбор пользователем порталов используемых для поиска"""

    choise_pars = input(f'Для поиска вакансий введите одно из значений:\n'
                        f'1 - поиск только на сайте HeadHanter\n'
                        f'2 - поиск только на сайте SuperJob\n'
                        f'{any_key()}поиск на обоих сайтах\n'
                        f'Ваш выбор: '
                        )

    if choise_pars == '1':
        hh = HHGetVacansies(vacansy)
        all_vacansies = hh.validate_vacansies()
    elif choise_pars == '2':
        sj = SJGetVacansies(vacansy)
        all_vacansies = sj.validate_vacansies()
    else:
        hh = HHGetVacansies(vacansy)
        sj = SJGetVacansies(vacansy)
        all_vacansies = hh.validate_vacansies()
        all_vacansies.extend(sj.validate_vacansies())

    return all_vacansies


def main():
    print("Здравствуйте!")
    vacansy = chose_vacancy()
    all_vacansies = enter_parsing(vacansy)
    print(len(all_vacansies))


if __name__ == '__main__':
    main()
