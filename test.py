import unittest
import main

class TestMaximumPathSum(unittest.TestCase):
    def test_no_layer(self):
        actual_sum = main.calculate_maximum_path_sum([])
        self.assertEqual(actual_sum, 0)

    def test_one_layer(self):
        actual_sum = main.calculate_maximum_path_sum([[3]])
        self.assertEqual(actual_sum, 3)

    def test_multi_layer_0(self):
        expected_sum = 1 + 2 + 6
        triangle = [[1], [2, 3], [6, 5, 4]]
        actual_sum = main.calculate_maximum_path_sum(triangle)
        self.assertEqual(actual_sum, expected_sum)

    def test_multi_layer_1(self):
        expected_sum = 2 + 3 + 4 + 100
        triangle = [[2], [2, 3], [50, 6, 4], [20, 8, 10, 100]]
        actual_sum = main.calculate_maximum_path_sum(triangle)
        self.assertEqual(actual_sum, expected_sum)


class TestParseTriangle(unittest.TestCase):
    TEST_DIR = "test_data/"

    def test_no_layer(self):
        actual_triangle = main.parse_triangle_file(f"{self.TEST_DIR}empty_triangle.txt")
        self.assertEqual(actual_triangle, [])

    def test_one_layer(self):
        actual_triangle = main.parse_triangle_file(f"{self.TEST_DIR}one_layer_triangle.txt")
        self.assertEqual(actual_triangle, [[48]])

    def test_multiple_layers(self):
        expected_triangle = [[1], [2, 3], [6, 5, 4]]
        actual_triangle = main.parse_triangle_file(f"{self.TEST_DIR}multi_layer_triangle.txt")
        self.assertEqual(actual_triangle, expected_triangle)


if __name__ == "__main__":
    unittest.main()
