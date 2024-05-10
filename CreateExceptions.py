class SomeError(Exception):  # Exception1
    pass


def some_function(x, y):
    if (isinstance(x, str) and isinstance(y, int)) or (isinstance(x, int) and isinstance(y, str)):
        raise SomeError('Нельзя складывать переменные разных типов')
    return x + y


print(some_function(10, 't'))


class AnotherError(Exception):  # Exception2
    pass


def another_function():
    a = 'login'
    b = 'password'

    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")

    if user_login != a or user_password != b:
        raise AnotherError('Неверный логин или пароль', {a: 'login', b: 'password'})
    else:
        print('Вы вошли')