import unittest
from sparta_sim.app.config_input import *

class test_data(unittest.TestCase):

    def test_correct_timeframe(self):
        self.assertIsInstance(months, int)
        self.assertIsInstance(years, int)
        self.assertEqual(total_time, (years*12)+months)


    # def test_gen_trainees(self):
    #     self.assertEqual(generate_trainees(), range(20, 31))
    #
    # def test_gen_centres(self):
    #     self.assertEqual(len(centres), months//2)
    #     ## first condition needs to be count of centres