import unittest
from src import SequenceFinder
import os


class TestSequenceFinder(unittest.TestCase):
    test_files_path = os.path.dirname(__file__) + "/files/"

    def setUp(self):
        self.sequenceFinder = SequenceFinder.SequenceFinder()

    def executeSequenceFinder_basicPipeline(self, file_name):
        self.sequenceFinder.read_input(self.test_files_path + file_name)
        return self.sequenceFinder.compute_sequence()

    def test_right_dimensions(self):
        self.sequenceFinder.read_input(self.test_files_path + "test06.txt")
        result = self.sequenceFinder.get_dimension()
        self.assertEqual(result, (4, 3))

    def test_right_matrix(self):
        self.sequenceFinder.read_input(self.test_files_path + "test03.txt")
        result = self.sequenceFinder.get_matrix()
        self.assertEqual(result, [[2, 1], [3, 4]])

    def test_right_matrix_asymmetrical_shape(self):
        self.sequenceFinder.read_input(self.test_files_path + "test06.txt")
        result = self.sequenceFinder.get_matrix()
        self.assertEqual(result, [[5, 8, 9], [6, 7, 1], [4, 3, 2], [10, 12, 13]])

    def test_case01(self):
        result = self.executeSequenceFinder_basicPipeline("test01.txt")
        self.assertEqual(result, [1, 2, 3, 4])

    def test_case02(self):
        result = self.executeSequenceFinder_basicPipeline("test02.txt")
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_case03(self):
        result = self.executeSequenceFinder_basicPipeline("test03.txt")
        self.assertEqual(result, [1, 2, 3, 4])

    def test_case04(self):
        result = self.executeSequenceFinder_basicPipeline("test04.txt")
        self.assertEqual(result, [5, 6, 7, 8, 9])

    def test_case05(self):
        result = self.executeSequenceFinder_basicPipeline("test05.txt")
        self.assertEqual(result, [5, 6, 7, 8, 9])

    def test_case06(self):
        result = self.executeSequenceFinder_basicPipeline("test06.txt")
        self.assertEqual(result, [5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()

