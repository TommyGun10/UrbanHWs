class Building:
    total = 0

    def __init__(self):
        Building.total += 1


city = []
city_size = 40
while len(city) < city_size:
    new_building = Building()
    city.append(new_building)
print(f'Total buildings in city is: {Building.total}')















