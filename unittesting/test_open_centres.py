import unittest
from mock_file import *

class TestCentre(unittest.TestCase):
    def test_centres(self):
        for i in centres:
            self.assertIsInstance(i, int)
            self.assertGreater(i, 0)
        
if __name__ == '__main__':
    unittest.main()