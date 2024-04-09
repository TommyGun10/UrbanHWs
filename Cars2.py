class Car:
    price = 1000000

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} - Цена:{}'.format(
            self.__class__.__name__, self.price)

    def horse_powers(self):
        print('123 лошадинные силы')


class Nissan(Car):
    price = 700000

    def horse_powers(self):
        print('110 лошадинных сил')


class Kia(Car):
    price = 1500000

    def horse_powers(self):
        print('150 лошадинных сил')


car1 = Nissan(name=None)
car2 = Kia(name=None)
print(car1)
car1.horse_powers()
print(car2)
car2.horse_powers()







