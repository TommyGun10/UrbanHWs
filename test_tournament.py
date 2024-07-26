import HW
import unittest


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = HW.Runner("Усэйн", speed=10)
        self.andrey = HW.Runner("Андрей", speed=9)
        self.nik = HW.Runner("Ник", speed=3)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            _result = {place: str(runner) for place, runner in result.items()}
            print(f"{key}: {_result}")

    def test_usain_nik(self):
        tournament = HW.Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results['test_usain_nik'] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_andrey_nik(self):
        tournament = HW.Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results['test_andrey_nik'] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_usain_andrey_nik(self):
        tournament = HW.Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results['test_usain_andrey_nik'] = results
        self.assertTrue(results[len(results)] == "Ник")


if __name__ == "__main__":
    unittest.main()
