from src.SequenceFinder import SequenceFinder

if __name__ == '__main__':
    sf = SequenceFinder()
    sf.read_input()
    solution = sf.compute_sequence()
    for i in solution[:-1]:
        print(i, end=" ")
    print(solution[-1], end="")
