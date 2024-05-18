def func_fabric(x, y):  # Фабрика функций
    if x > y:
        return x / y
    elif x == y:
        return 1
    else:
        return 0
print(func_fabric(1, 2))


square = lambda i: i ** 2 # Лямбда - функции, с аналогом def()
print(square(5))


def square_def(i):
    return i ** 2
print(square_def(5))


class Rect: # Вызывавемые объекты
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return b * self.a

side = Rect(a=15)
result = side(b=20)
print(result)
