import unittest
# from sparta_sim.app import Abi
from sparta_sim.app import config_input
# from unittesting import idk


class TestIdk(unittest.TestCase):

    """ This was just a file I created to do small refactoring to test if my unittests work
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
    """
    """
    def test_generate_trainees(self):
        for number in Abi.generate_trainees():
            self.assertIn(Abi, list(range(20, 31)))
            # return number
        for number in Abi.generate_trainees():
            self.assertIn(number, list(range(20, 31)))
            # return number
        for number in Abi.generate_trainees():
            self.assertIn(number, list(range(20, 31)))
            # return number

    def test_generate_training_centres(self):

        # Testing the output which should equal the months divided by 2 plus 1 which is the centre already open initially
        self.assertEqual(Abi.generate_training_centres(1), 1)
        self.assertEqual(Abi.generate_training_centres(2), 2)
        self.assertEqual(Abi.generate_training_centres(10), 6)

    def test_generate_full_centres(self):

        # Testing that training centres get full to 100
        self.assertLessEqual(Abi.generate_full_centres("months"), 100)
        self.assertLessEqual(Abi.generate_full_centres("months"), 100)

    def test_trainee_list(self):

        # List in this instance must be twelve and remain at twelve
        self.assertEqual(len(file_name.trainee_list('months')), 12)

    def test_waiting_trainees(self):

        # Testing that the trainee waiting list if greater than 0 at all times
        self.assertGreaterEqual(Abi.waiting_trainees(), 0)

        # If all centres all full, then waiting list cannot equal 0
        for values in centres_dictionary:
            if the_number_of_keys * 100 == number of trainees:
                self.assertNotEqual(Abi.waiting_trainees('months'), 0)
"""
    def test_config_input(self):
        self.assertRaises(ValueError, config_input.months, 'k')
        self.assertRaises(ValueError, config_input.years, 'k')


if __name__ == '__main__':
    unittest.main()

