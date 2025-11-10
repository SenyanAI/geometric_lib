import unittest
class SquareTestCase(unittest.TestCase):
    def test_area_ten_side(self):
        res = area(10)
        expected = 10 * 10
        self.assertEqual(res, expected)
    def test_area_twenty_five_side(self):
        res = area(25)
        expected = 25 * 25
        self.assertEqual(res, expected)
    def test_perimeter_fifteen_side(self):
        res = perimeter(15)
        expected = 4 * 15
        self.assertEqual(res, expected)
    def test_perimeter_thirty_side(self):
        res = perimeter(30)
        expected = 4 * 30
        self.assertEqual(res, expected)
