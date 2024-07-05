import unittest
from UnitTests import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student1 = Student("Alice")
        self.student2 = Student("Bob")

    def test_walk_10_times(self):
        for _ in range(10):
            self.student1.walk()
        self.assertEqual(self.student1.distance, 50,
                         msg="Дистанции не равны {} != 500".format(self.student1.distance))

    def test_run_10_times(self):
        for _ in range(10):
            self.student2.run()
        self.assertEqual(self.student2.distance, 100,
                         msg="Дистанции не равны {} != 1000".format(self.student2.distance))

    def test_running_vs_walking(self):
        for _ in range(10):
            self.student1.run()
            self.student2.walk()
        self.assertGreater(self.student2.distance, self.student1.distance,
                           msg="{} должен преодолеть дистанцию больше, чем {}"
                           .format(self.student2.name, self.student1.name))


if __name__ == '__main__':
    unittest.main()
    