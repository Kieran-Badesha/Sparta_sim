import unittest

from sparta_sim.app import Abi
# from unittesting import idk


class TestIdk(unittest.TestCase):

    # def test_generate_trainees(self):
    #     for number in idk.generate_trainees(1):
    #         self.assertIn(number, list(range(20, 31)))
    #         return number
    #     for number in idk.generate_trainees(5):
    #         self.assertIn(number, list(range(20, 31)))
    #         return number
    #     for number in idk.generate_trainees(200):
    #         self.assertIn(number, list(range(20, 31)))
    #         return number

    def test_generate_trainees(self):
        for number in Abi.generate_trainees():
            self.assertIn(Abi, list(range(20, 31)))
            return number
        for number in Abi.generate_trainees():
            self.assertIn(number, list(range(20, 31)))
            return number
        for number in Abi.generate_trainees():
            self.assertIn(number, list(range(20, 31)))
            return number

    def test_generate_training_centres(self):
        self.assertEqual(Abi.generate_training_centres(1), 1)
        self.assertEqual(Abi.generate_training_centres(2), 2)
        self.assertEqual(Abi.generate_training_centres(10), 6)

    # def test_waiting_trainees(self):
    #     self.assertGreaterEqual(Abi.waiting_trainees(), 0)


if __name__ == '__main__':
    unittest.main()

