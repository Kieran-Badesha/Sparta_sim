import unittest
from sparta_sim.app.Abi import *

class test_gen(unittest.TestCase):

    def test_gen_trainees(self):
        self.assertEqual(generate_trainees(), range(20, 31))

    def test_gen_centres(self):
        self.assertEqual(len(centres), months//2)
        ## first condition needs to be count of centres