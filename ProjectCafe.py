import threading
import time

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.queue = []
        self.tables = tables

    def customer_arrival(self):
        for i in range(1, 21):  
            time.sleep(1)
            print(f"Посетитель номер {i} прибыл.")
            customer = threading.Thread(target=self.serve_customer, args=(i,))
            customer.start()

    def serve_customer(self, customer_number):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer_number} сел за стол {table.number}. (начало обслуживания)")
                time.sleep(5)
                print(f"Посетитель номер {customer_number} покушал и ушёл. (конец обслуживания)")
                table.is_busy = False
                break
        else:
            self.queue.append(customer_number)
            print(f"Посетитель номер {customer_number} ожидает свободный стол. (помещение в очередь)")

class Customer:
    def __init__(self, cafe):
        self.cafe = cafe

    def run(self):
        while True:
            while self.cafe.queue:
                customer_number = self.cafe.queue.pop(0)
                for table in self.cafe.tables:
                    if not table.is_busy:
                        table.is_busy = True
                        print(f"Посетитель номер {customer_number} сел за стол {table.number}. (начало обслуживания)")
                        time.sleep(5)
                        print(f"Посетитель номер {customer_number} покушал и ушёл. (конец обслуживания)")
                        table.is_busy = False
                        break

tables = [Table(1), Table(2), Table(3)]
cafe = Cafe(tables)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]


customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_thread = Customer(cafe)
customer_thread.run()
