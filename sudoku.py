class Sudoku:
    def __init__(self, table: list):
        self.table = table
        self.maked_table = []

    def print_table(self):
        for row in self.table:
            print('-------------------------------------')
            for col in row:
                print('| {} '.format(col), end='')

            print('|')
        print('-------------------------------------')

    def find_empty(self):
        row_len = len(self.table)
        col_len = len(self.table[0])

        for i in range(row_len):
            for j in range(col_len):
                if self.table[i][j] == ' ':
                    return (i, j)

        return False

    def is_empty(self):
        pass

    def __is_valid(self, p: tuple, number):
        number = str(number)

        # Fila
        for j in range(len(self.table[0])):
            if number == self.table[p[0]][j] and j != p[1]:
                return False

        # Columna
        for i in range(len(self.table)):
            if number == self.table[i][p[1]] and i != p[0]:
                return False

        i_label = p[0] // 3
        j_label = p[1] // 3
        for ii in range(len(self.table)):
            for jj in range(len(self.table[0])):
                if (ii // 3 == i_label and jj // 3 == j_label) and \
                        number == self.table[ii][jj] and (ii, jj) != p:
                    return False

        return True

    def __what_number(self, p):
        for number in range(1, len(self.table[0])+1):
            valid = self.__is_valid(p, number)
            if valid == True:
                return valid, number

        return valid, 0

    def __backtracking(self, s: tuple):
        if s[0] == len(self.table) or s[1] == len(self.table[0]):
            go_on = True
        else:
            go_on = False

        number = 1
        while number <= len(self.table) and go_on == False:
            if self.table[s[0]][s[1]] == ' ':
                self.table[s[0]][s[1]] = str(number)

                if self.__is_valid(s, number):
                    # self.print_table()
                    if s[0] < len(self.table)-1 and s[1] < len(self.table[0]):
                        i = s[0] if s[1] < len(self.table[0])-1 else s[0]+1
                        j = s[1]+1 if s[1] < len(self.table[0])-1 else 0

                        go_on = self.__backtracking((i, j))
                    else:
                        self.maked_table = self.table.copy()
                        go_on = True

                self.table[s[0]][s[1]] = ' '
                number += 1

            else:
                i = s[0] if s[1] < len(self.table[0])-1 else s[0]+1
                j = s[1]+1 if s[1] < len(self.table[0])-1 else 0

                s = (i, j)

            if s[0] == len(self.table):
                go_on = True
                break

        return go_on

    def solve(self):
        return self.__backtracking((0, 0))
