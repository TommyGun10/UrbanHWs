class House:
    def __init__(self):
        self.numberOfFloors = 10


house = House()
floor = 1
while floor <= house.numberOfFloors:
    print(f'Текущий этаж равен {floor}')
    floor += 1


