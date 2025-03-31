# test.py

import unittest
from math_operations import add, subtract, multiply, divide
from shapes.circle import area as circle_area, circumference as circle_circumference
from shapes.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from shapes.triangle import area as triangle_area, perimeter as triangle_perimeter

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), None)
        self.assertEqual(divide(0, 5), 0)

class TestShapes(unittest.TestCase):
    def test_circle(self):
        self.assertAlmostEqual(circle_area(5), 78.54, places=2)
        self.assertAlmostEqual(circle_circumference(5), 31.42, places=2)

    def test_rectangle(self):
        self.assertEqual(rectangle_area(4, 6), 24)
        self.assertEqual(rectangle_perimeter(4, 6), 20)

    def test_triangle(self):
        self.assertEqual(triangle_area(3, 4), 6)
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

if __name__ == '__main__':
    unittest.main()