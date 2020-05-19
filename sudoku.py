from colors import *


class Sudoku:
    def __init__(self, table: list):
        self.__table = table
        self.__maked_table = []
        self.__row_len = len(self.__table)
        self.__col_len = len(self.__table[0])

    '''
    Asinga el color a un dependiendo de su posición
    '''

    def __assign_color(self, s):
        i_key = s[0] // 3
        j_key = s[1] // 3

        return colors[str(i_key) + str(j_key)]

    '''
    Imprime el arreglo, con formato
    '''

    def print_table(self):
        for i in range(self.__row_len):
            print('-------------------------------------')
            for j in range(self.__col_len):
                print('| {}{}{} '.format(
                    self.__assign_color((i, j)),
                    self.__maked_table[i][j],
                    RESET
                ), end='')

            print('|')
        print('-------------------------------------')

    def __is_empty(self, s: tuple) -> bool:
        return True if self.__table[s[0]][s[1]] == ' ' else False

    def __is_valid(self, s: tuple, number: int) -> bool:
        number = str(number)

        # Fila
        for j in range(len(self.__table[0])):
            if number == self.__table[s[0]][j] and j != s[1]:
                return False

        # Columna
        for i in range(len(self.__table)):
            if number == self.__table[i][s[1]] and i != s[0]:
                return False

        # Region
        i_label = s[0] // 3
        j_label = s[1] // 3
        for ii in range(len(self.__table)):
            for jj in range(len(self.__table[0])):
                if (ii // 3 == i_label and jj // 3 == j_label) and \
                        number == self.__table[ii][jj] and (ii, jj) != s:
                    return False

        return True

    def __change_position(self, s: tuple) -> tuple:
        i = s[0] if s[1] < self.__col_len-1 else s[0]+1
        j = s[1]+1 if s[1] < self.__col_len-1 else 0

        return (i, j)

    def __copy_table(self):
        for row in self.__table:
            self.__maked_table.append(row.copy())

    def __backtracking(self, s: tuple) -> bool:
        if s == (self.__row_len, self.__col_len-1):
            go_on = True
        else:
            go_on = False

        number = 1
        while number <= self.__col_len and go_on == False:
            if self.__is_empty(s):
                self.__table[s[0]][s[1]] = str(number)

                if self.__is_valid(s, number):

                    if s == (self.__row_len-1, self.__col_len-1):
                        self.__copy_table()
                        go_on = True

                    else:
                        go_on = self.__backtracking(self.__change_position(s))

                self.__table[s[0]][s[1]] = ' '
                number += 1
            else:
                if s == (self.__row_len-1, self.__col_len-1):
                    self.__copy_table()
                    go_on = True

                else:
                    s = self.__change_position(s)

        return go_on

    def solve(self):
        return self.__backtracking((0, 0))


class SudokuSamurai:
    def __init__(self, maked_table):
        pass
