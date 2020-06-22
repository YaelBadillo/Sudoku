from tables import *
from sudoku import SamuraiSudoku


def main():
    sudoku = SamuraiSudoku(TABLA_1)
    sudoku.solve()
    sudoku.print_maked_table()


if __name__ == '__main__':
    main()
