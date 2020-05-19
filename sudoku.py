from colors import *


class Sudoku:
    def __init__(self, table: list):
        self.table = table
        self.maked = []
        self.row_len = len(self.table)
        self.col_len = len(self.table[0])

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
        for i in range(self.row_len):
            print('-------------------------------------')
            for j in range(self.col_len):
                print('| {}{}{} '.format(
                    self.__assign_color((i, j)),
                    self.maked[i][j],
                    RESET
                ), end='')

            print('|')
        print('-------------------------------------')

    def __is_empty(self, s: tuple) -> bool:
        return True if self.table[s[0]][s[1]] == ' ' else False

    def __is_valid(self, s: tuple, number: int) -> bool:
        number = str(number)

        # Fila
        for j in range(len(self.table[0])):
            if number == self.table[s[0]][j] and j != s[1]:
                return False

        # Columna
        for i in range(len(self.table)):
            if number == self.table[i][s[1]] and i != s[0]:
                return False

        # Region
        i_label = s[0] // 3
        j_label = s[1] // 3
        for ii in range(len(self.table)):
            for jj in range(len(self.table[0])):
                if (ii // 3 == i_label and jj // 3 == j_label) and \
                        number == self.table[ii][jj] and (ii, jj) != s:
                    return False

        return True

    def __change_position(self, s: tuple) -> tuple:
        i = s[0] if s[1] < self.col_len-1 else s[0]+1
        j = s[1]+1 if s[1] < self.col_len-1 else 0

        return (i, j)

    def __copy_table(self):
        for row in self.table:
            self.maked.append(row.copy())

    def __backtracking(self, s: tuple) -> bool:
        if s == (self.row_len, self.col_len-1):
            go_on = True
        else:
            go_on = False

        number = 1
        while number <= self.col_len and go_on == False:
            if self.__is_empty(s):
                self.table[s[0]][s[1]] = str(number)

                if self.__is_valid(s, number):

                    if s == (self.row_len-1, self.col_len-1):
                        self.__copy_table()
                        go_on = True

                    else:
                        go_on = self.__backtracking(self.__change_position(s))

                self.table[s[0]][s[1]] = ' '
                number += 1
            else:
                if s == (self.row_len-1, self.col_len-1):
                    self.__copy_table()
                    go_on = True

                else:
                    s = self.__change_position(s)

        return go_on

    def solve(self):
        return self.__backtracking((0, 0))
