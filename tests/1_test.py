from main import print_Hello
import unittest
 
class test_1(unittest.TestCase):

    def test_1_Hello(self):
        result = print_Hello()
        self.assertEqual(result,"hello")
