def test(*args):
    for i, arg in enumerate(args):
        print(f'На позиции {i}: {arg}')


test(20, 80.5, "okay", True)


def factorial(n):
    if n == 1:
        return 1
    factorial_low = factorial(n=n - 1)
    return n * factorial_low


print('Factorial 10 =', factorial(10))
