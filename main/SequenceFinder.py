import fileinput
from Direction import Direction

class SequenceFinder:
    def __init__(self):
        self.lines, self.cols = 0, 0
        self.matrix = []

    def read_input(self, file_name):
        with fileinput.input(files=file_name) as file01:
            self.lines, self.cols = file01.readline().split(" ")
            self.lines = int(self.lines)
            self.cols = int(self.cols)

            for line in range(self.lines):
                matrix_line = [int(x) for x in file01.readline().strip().split(" ")]
                self.matrix.append(matrix_line)
            file01.close()

    def compute_sequence(self):
        for line in range(self.lines):
            for col in range(self.cols):
                pass

    def __check_neighbor(self, actual_coords, previous_value=None, incoming_direction=Direction.STAND):
        pass

    def get_dimension(self):
        return self.lines, self.cols

    def get_matrix(self):
        return self.matrix

if __name__ == '__main__':
    sf = SequenceFinder()
    sf.read_input("../files/test01.txt")
