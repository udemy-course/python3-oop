
import unittest

from s13_debug_unittest.main.math_func import add


class TestAdd(unittest.TestCase):


    def setUp(self):
        self.a = 10
        self.b = 20

    def test_add(self):

        self.assertEqual(add(self.a, self.b), 30)

    def tearDown(self):
        del self.a
        del self.b

if __name__ == "__main__":

    unittest.main()
