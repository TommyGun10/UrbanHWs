import threading
import time


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        self.lock.acquire()
        try:
            while self.balance < 1000:
                self.balance += amount
                print(f"Пополнение {amount} рублей. Ваш баланс: {self.balance}")
                time.sleep(0.5)
        finally:
            self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        try:
            while self.balance > 0:
                self.balance -= amount
                print(f"Вывод {amount} рублей. Ваш баланс: {self.balance}")
                time.sleep(0.5)
        finally:
            self.lock.release()


account = BankAccount(balance=100)


thread1 = threading.Thread(target=account.deposit, args=(150,))
thread2 = threading.Thread(target=account.withdraw, args=(100,))


thread1.start()
thread2.start()

thread1.join()
thread2.join()






