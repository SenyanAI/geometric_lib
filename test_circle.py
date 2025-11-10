import unittest
class CircleTestCase(unittest.TestCase):
    def test_area_ten_radius(self):
        res = area(10)
        expected = math.pi * 10 * 10
        self.assertAlmostEqual(res, expected)
    def test_area_twenty_five_radius(self):
        res = area(25)
        expected = math.pi * 25 * 25
        self.assertAlmostEqual(res, expected)
    def test_perimeter_fifteen_radius(self):
        res = perimeter(15)
        expected = 2 * math.pi * 15
        self.assertAlmostEqual(res, expected)
    def test_perimeter_thirty_radius(self):
        res = perimeter(30)
        expected = 2 * math.pi * 30
        self.assertAlmostEqual(res, expected)
