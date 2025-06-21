import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculator(unittest.TestCase):
    def setUp(self):
        # "setting up the simple calculator instance for each arithmetic
        self.calc = SimpleCalculator()
    def test_addition(self):
        # Test the addition method
        self.assertEqual(self.calc.add(2,3) ,5)
        self.assertEqual(self.calc.add(-1,1), 0) 

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,3) ,-1)
        self.assertEqual(self.calc.subtract(5,4) ,1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,4),8)
        self.assertEqual(self.calc.multiply(0,1),0)  

    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(12,-2),10)             