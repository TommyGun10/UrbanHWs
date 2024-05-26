import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill

    def run(self):
        days = 0
        enemies = 100

        while enemies > 0:
            print(f"{self.name} защищает королевство от {enemies} врагов.")
            enemies -= self.skill
            days += 1
            time.sleep(1.5)  

        print(f"{self.name} защищает королевство в течении {days} дней.")


print('На нас напали!')
knight1 = Knight("Dragon Knight", 20)
knight2 = Knight("Sven", 10)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Оба рыцаря успешно одолели врагов.")





