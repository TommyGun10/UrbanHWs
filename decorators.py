from math import sqrt


def is_prime(func):
    def wrapper():
        sum1 = func()
        prime = True

        i = 2
        while i <= sqrt(sum1):
            if sum1 % i == 0:
                prime = False
                break
            i += 1

        if prime:
            print(f'{sum1} является простым числом')
        else:
            print(f'{sum1} является составным числом')
    return wrapper


@is_prime
def sum_three():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    sum1 = a + b + c
    return sum1


sum_three()

