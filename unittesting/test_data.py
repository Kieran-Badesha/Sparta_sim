import unittest
#from sparta_sim.app.config_input import *
from sparta_sim.app.Abi import waiting_list, centre, trainees


class test_data(unittest.TestCase):

    ## Tests whether months and years are integer values and total time is correct value
    #def test_correct_timeframe(self):
    #    self.assertIsInstance(months, int)
    #    self.assertIsInstance(years, int)
    #    self.assertEqual(total_time, (years * 12) + months)

    # Tests whether the waiting list is actually a list and all values are non-negative
    def test_waiting_list(self):
        self.assertIsInstance(waiting_list, list)
        try:
            self.assertGreaterEqual(min(waiting_list), 0)
        except:
            print("List is empty")

    # Tests whether the number of trainees at each centre is an integer, non-negative and less than 100
    def test_populous_centre(self):
        for i in centre.values():
            self.assertIsInstance(i, int)
            self.assertGreaterEqual(i, 0)
            self.assertLessEqual(i, 100)

    # Checks that the output of trainees each month is a list and is a number between 20 and 30
    def test_trainees_month(self):
        self.assertIsInstance(trainees, list)
        for i in trainees:
            self.assertIsInstance(i, int)
            self.assertGreaterEqual(i, 20)
            self.assertLessEqual(i, 30)


    # # Tests the number of centres being equal to the floor division of number of months over 2
    # def test_gen_centres(self):
    #     self.assertEqual(len(centres), months//2)