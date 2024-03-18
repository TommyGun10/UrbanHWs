def test(*args):
    for i, arg in enumerate(args):
        print(f'На позиции {i}: {arg}')


test(20, 80.5, "okay", True)


def factorial(n):
    if n == 0:
        return 1
    factorial_low = factorial(n=n - 1)
    return n * factorial_low


a = int(input('Введите число для рассчета факториала: '))
print(f"Факториал числа {a} равен {factorial(a)}")
