import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter


class TestCircle(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(circle_area(1), math.pi, places=5)
        self.assertAlmostEqual(circle_area(2.5), math.pi * 2.5 * 2.5, places=5)

    def test_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi, places=5)
        self.assertAlmostEqual(circle_perimeter(3), 2 * math.pi * 3, places=5)


class TestSquare(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square_area(2), 4)
        self.assertEqual(square_area(5), 25)

    def test_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square_perimeter(2), 8)
        self.assertEqual(square_perimeter(5), 20)
