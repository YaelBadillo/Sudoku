from table import TABLE, T2
from sudoku import Sudoku


def main():
    s1 = Sudoku(TABLE[:])
    s1.solve()
    # s1.print_table()


if __name__ == '__main__':
    main()
