from table import *
from sudoku import SamuraiSudoku


def main():
    s1 = SamuraiSudoku(samurai)
    s1.solve()
    s1.print_table()


if __name__ == '__main__':
    main()
