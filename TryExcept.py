def string_to_int(s):     # добавить обработку ValueError
    try:
        return int(s)
    except ValueError as ValErr:
       return f'Ошибка {ValErr}: Невозможно преобразовать "{s}" в целое число'


def read_file(filename):     # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f'Ошибка: Не удается найти файл "{filename}".'
    except IOError:
        return f'Ошибка ввода/вывода при работе с файлом "{filename}".'


def divide_numbers(a, b):     # добавить обработку ZeroDivisionError, TypeError
    try:
        return a / b
    except ZeroDivisionError as exc:
        return f'Ошибка {exc}: Нельзя делить на ноль.'
    except TypeError as exc2:
        return f'Ошибка {exc2}: аргументы должны быть числами.'


def access_list_element(lst, index):     # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return f'Ошибка: индекс {index} вне диапазона списка.'
    except TypeError:
        return f'Ошибка: индекс должен быть целым числом'
