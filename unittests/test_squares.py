import unittest

class TestGeometryLibrary(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(GeometryLibrary.circle_area(2), 12.5663706144, places=5)

    def test_triangle_area(self):
        self.assertAlmostEqual(GeometryLibrary.triangle_area(3, 4, 5), 6.0, places=5)

    def test_is_right_triangle(self):
        self.assertTrue(GeometryLibrary.is_right_triangle(3, 4, 5))
        self.assertFalse(GeometryLibrary.is_right_triangle(1, 2, 3))

if __name__ == "__main":
    unittest.main()
