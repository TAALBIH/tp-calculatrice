
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculatrice import addition, soustraction, multiplication, division

import unittest
class TestCalculatrice(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)

    def test_soustraction(self):
        self.assertEqual(soustraction(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 5), 10)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(10, 0)

if __name__ == "__main__":
    unittest.main()
