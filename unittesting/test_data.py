import unittest
from sparta_sim.app.config_input import *
from sparta_sim.app.Abi import waiting_trainees, waiting_list


class test_data(unittest.TestCase):

    # Tests whether months and years are integer values and total time is correct value
    def test_correct_timeframe(self):
        self.assertIsInstance(months, int)
        self.assertIsInstance(years, int)
        self.assertEqual(total_time, (years * 12) + months)

    def test_waiting_list(self):
        self.assertIsInstance(waiting_list, list)
        try:
            self.assertGreaterEqual(min(waiting_list), 0)
        except:
            print("List is empty")

    # def test_gen_trainees(self):
    #     self.assertEqual(generate_trainees(), range(20, 31))
    #
    # def test_gen_centres(self):
    #     self.assertEqual(len(centres), months//2)
    #     ## first condition needs to be count of centres
