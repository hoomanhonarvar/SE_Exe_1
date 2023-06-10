from main import print_hi
import unittest
 
class test_1(unittest.TestCase):

    def test_1_Hello(self):
        result = print_hi()
        self.assertEqual(result,"hi")
