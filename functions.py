def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    matches = []
    for contact in book:
        if info in contact:
            matches.append(contact)

    num_matches = len(matches)
    if num_matches == 0:
        return 'Совпадений не найдено'
    elif num_matches == 1:
        return matches[0]
    else:
        print('Найдено несколько совпадений:')
        for i, match in enumerate(matches, start=1):
            print(f'{i}. {match}')

        while True:
            choice = input('Введите номер желаемого совпадения: ')
            if choice.isdigit() and 1 <= int(choice) <= num_matches:
                return matches[int(choice) - 1]
            else:
                print('Неверный выбор. Пожалуйста, введите корректный номер.')

def update_contact(book: str, name: str, new_contact: str) -> str:
    """Обновляет контакт в телефонном справочнике по имени или фамилии"""
    lines = book.split('\n')
    updated_lines = []
    for line in lines:
        if name.lower() in line.lower():
            updated_lines.append(new_contact)
        else:
            updated_lines.append(line)
    updated_book = '\n'.join(updated_lines)
    return updated_book

def delete_contact(book: str, name: str) -> str:
    """Удаляет контакт из телефонного справочника по имени или фамилии"""
    lines = book.split('\n')
    updated_lines = []
    for line in lines:
        if name.lower() not in line.lower():
            updated_lines.append(line)
    updated_book = '\n'.join(updated_lines)
    return updated_book
