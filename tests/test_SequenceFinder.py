import unittest

from main import SequenceFinder

class TestSequenceFinder(unittest.TestCase):

    def setUp(self) -> None:
        print("Creating new SequenceFinder...")
        self.sequenceFinder = SequenceFinder.SequenceFinder()

    def test_case01(self):
        self.sequenceFinder.read_input("test01.txt")
        result = self.sequenceFinder.compute_sequence()
        self.assertEqual(result, [1, 2, 3, 4])

    def test_case02(self):
        self.sequenceFinder.read_input("test02.txt")
        result = self.sequenceFinder.compute_sequence()
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_case03(self):
        self.sequenceFinder.read_input("test03.txt")
        result = self.sequenceFinder.compute_sequence()
        self.assertEqual(result, [1, 2, 3, 4])

    def test_case04(self):
        self.sequenceFinder.read_input("test04.txt")
        result = self.sequenceFinder.compute_sequence()
        self.assertEqual(result, [5, 6, 7, 8, 9])

    def test_case05(self):
        self.sequenceFinder.read_input("test05.txt")
        result = self.sequenceFinder.compute_sequence()
        self.assertEqual(result, [5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()