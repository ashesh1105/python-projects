import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-2, 3), 1)
        self.assertEqual(calc.add(-5, -7), -12)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.subtract(12, 3), 9)
        self.assertEqual(calc.subtract(-2, -3), 1)

    def test_divide_floor(self):
        self.assertEqual(calc.divide_floor(6, 3), 2)
        self.assertEqual(calc.divide_floor(-12, 3), -4)
        self.assertEqual(calc.divide_floor(18, -3), -6)
        self.assertEqual(calc.divide_floor(5, 2), 2)

    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(-12, 3), -4)
        self.assertEqual(calc.divide(18, -3), -6)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # Note how we test an exception raised! Order of arguments is important here:
        # Expected Exception -> function (with no arguments) -> arguments that function will take
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # If you want to avoid calling function in above way instead of normal way: calc.divide(10, 0),
        # you need to use ContextManager in below way:
        with self.assertRaises(ValueError):
            calc.divide(10, 0)




# Below will allow this test file to be run a simple python file: python test_calc.py
if __name__ == '__main__':
    unittest.main()




