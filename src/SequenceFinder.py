import fileinput
from src.Direction import Direction
from utils.utils import check_complementary


class SequenceFinder:
    """
    A class used to solve a (single) instance of a Matrix Sequence Problem
    ...
    Attributes
    ----------
    __lines : int
        The number of lines of the solving matrix
    __cols : int
        The number of columns of the solving matrix
    __matrix : list[[int]]
        The matrix of this problem's instance
    __memo_matrix : list[[int]]
        Matrix of equal shape as __matrix, used for memoization
    __biggest_sequence : list[int]
        Current biggest sequence found
    """

    def __init__(self):
        self.__lines, self.__cols = 0, 0
        self.__matrix = []
        self.__memo_matrix = []
        self.__biggest_sequence = []

    def read_input(self, file_name=None):
        """Reads the given input obtained from a file (given the file path), or when not provided, from the standard
        input

        Parameters
        ----------
        file_name : str
            Path to the file to be read
        """

        with fileinput.input(files=file_name) as file01:
            self.__lines, self.__cols = file01.readline().split(" ")
            self.__lines = int(self.__lines)
            self.__cols = int(self.__cols)

            for line in range(self.__lines):
                matrix_line = [int(x) for x in file01.readline().strip().split(" ")]
                self.__matrix.append(matrix_line)

            self.__memo_matrix = [[None for _ in range(self.__cols)] for _ in range(self.__lines)]
            file01.close()

    def compute_sequence(self):
        """Iterates the previously obtained matrix to find the biggest sequence of successive numbers

        Returns
        ----------
        list[int]
            The biggest sequence obtained during the computation
        """
        for line in range(self.__lines):
            for col in range(self.__cols):
                t_sequence = self.__check_neighbor((line, col))
                if len(t_sequence) > len(self.__biggest_sequence):
                    self.__biggest_sequence = t_sequence
        return self.__biggest_sequence

    def __check_neighbor(self, actual_coords, previous_value=None, incoming_direction=None):
        """Checks if given point in matrix can be part of a sequence following a previous, adjacent point
        Parameters
        ----------
        actual_coords : (int, int)
            Actual coordinates under analysis, in the form of (line, column)
        previous_value : int
            Value existent in the previous point of the matrix, adjacent to the current point
        incoming_direction : Direction
            Direction from which the current point was reached
        Returns
        ----------
        list[int]
            A list containing a subset of successive values in the current chain
        """
        result = []
        # stop condition 1: check margins
        if actual_coords[0] < 0 or actual_coords[1] < 0 or actual_coords[0] >= self.__lines or actual_coords[1] \
                >= self.__cols:
            return result

        # stop condition 2: check increment of +1
        if previous_value and self.__matrix[actual_coords[0]][actual_coords[1]] != previous_value + 1:
            return result

        # if current point was already explored, it is possible to check how far is reaches from here
        if self.__memo_matrix[actual_coords[0]][actual_coords[1]]:
            initial_value = self.__matrix[actual_coords[0]][actual_coords[1]]
            chain_reach = self.__memo_matrix[actual_coords[0]][actual_coords[1]]
            # capitalizing on the fact that if a chain exists, it consists of an increment of +1 for every element
            result = [j for j in range(initial_value, initial_value + chain_reach)]
            return result

        else:
            for outcoming_direction in Direction:
                # going back to incoming direction would lead to infinite cycles
                if not incoming_direction or not check_complementary(incoming_direction.value, outcoming_direction.value):
                    result += self.__check_neighbor((actual_coords[0] + outcoming_direction.value[0], actual_coords[1] +
                                                     outcoming_direction.value[1]),
                                                    self.__matrix[actual_coords[0]][actual_coords[1]],
                                                    outcoming_direction)

                    # since numbers are unique, if a chain was found, there is no need to keep looking from the current
                    # point
                    if result:
                        break

        # add actual point to chain obtained backwards
        current_chain = [self.__matrix[actual_coords[0]][actual_coords[1]]] + result
        self.__memo_matrix[actual_coords[0]][actual_coords[1]] = len(current_chain)

        return current_chain

    def get_dimension(self):
        """

        Returns
        ----------
        (int, int)
            Dimension of the obtained matrix, in the form of (number of lines, number of columns)
        """
        return self.__lines, self.__cols

    def get_matrix(self):
        """

        Returns
        ----------
        list[[int]]
            Returns the matrix of this problem's instance, or [] if it was not yet set
        """
        return self.__matrix

    def get_sequence(self):
        """

        Returns
        ----------
        list[int]
            Returns the solution of this problem's instance, or [] if it was not yet computed
        """
        return self.__biggest_sequence
