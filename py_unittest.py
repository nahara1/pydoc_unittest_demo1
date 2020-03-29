import calculator
import unittest


class TestOperationsMethods(unittest.TestCase):

    def test_addition(self):
        value = calculator.add(1, 2)
        self.assertEqual(3, value)

    def test_subtraction(self):
        value = calculator.subtract(1, 2)
        self.assertEqual(-1, value)

    def test_multiplication(self):
        value = calculator.multiply(1, 2)
        self.assertEqual(2, value)

    def test_division(self):
        value = calculator.divide(1, 2)
        self.assertEqual(0.5, value)


if __name__ == '__main__':
    unittest.main()
