import unittest

from main import SequenceFinder

class TestSequenceFinder(unittest.TestCase):

    def setUp(self) -> None:
        print("Creating new SequenceFinder...")
        self.sequenceFinder = SequenceFinder.SequenceFinder()

    def executeSequenceFinder_basicPipeline(self, file_name):
        self.sequenceFinder.read_input(file_name)
        return self.sequenceFinder.compute_sequence()

    def test_case01(self):
        print("Executing Test01...")
        result = self.executeSequenceFinder_basicPipeline("test01.txt")
        self.assertEqual(result, [1, 2, 3, 4])

    def test_case02(self):
        print("Executing Test02...")
        result = self.executeSequenceFinder_basicPipeline("test02.txt")
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_case03(self):
        print("Executing Test03...")
        result = self.executeSequenceFinder_basicPipeline("test03.txt")
        self.assertEqual(result, [1, 2, 3, 4])

    def test_case04(self):
        print("Executing Test04...")
        result = self.executeSequenceFinder_basicPipeline("test04.txt")
        self.assertEqual(result, [5, 6, 7, 8, 9])

    def test_case05(self):
        print("Executing Test05...")
        result = self.executeSequenceFinder_basicPipeline("test05.txt")
        self.assertEqual(result, [5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()