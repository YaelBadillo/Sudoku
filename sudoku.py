from colors import *


class Sudoku:
    def __init__(self, board: list):
        self.__board = board                            # Tabla sin hacer
        self.__maked_board = []                         # Tabla hecha
        self.__row_len = len(self.__board)              # Número de las FILAS
        self.__col_len = len(self.__board[0])           # Número de COLUMNAS

    def get_row_len(self):
        return self.__row_len

    def get_col_len(self):
        return self.__col_len

    def get_board(self) -> list:
        return self.__board

    def get_maked_board(self) -> list:
        return self.__maked_board

    ''' __assign_color()
    Asinga el color a un numero dependiendo su posición s = (i, j)
    '''

    def __assign_color(self, s) -> str:
        i_key = s[0] // 3
        j_key = s[1] // 3

        return colors[str(i_key) + str(j_key)]

    ''' print_board()
    Imprime la tabla inicial, con formato
    '''

    def print_board(self):
        for i in range(self.__row_len):
            print('-------------------------------------')
            for j in range(self.__col_len):
                print('| {}{}{} '.format(
                    self.__assign_color((i, j)),
                    self.__board[i][j],
                    RESET
                ), end='')

            print('|')
        print('-------------------------------------')

    ''' print_maked_board()
    Imprime la tabla llena, con formato
    '''

    def print_maked_board(self):
        for i in range(self.__row_len):
            print('-------------------------------------')
            for j in range(self.__col_len):
                print('| {}{}{} '.format(
                    self.__assign_color((i, j)),
                    self.__maked_board[i][j],
                    RESET
                ), end='')

            print('|')
        print('-------------------------------------')

    ''' ___is_empty()
    Verifica si la posición s = (i, j) del tablero self.__board,
    está vacía
    '''

    def __is_empty(self, s: tuple) -> bool:
        return True if self.__board[s[0]][s[1]] == ' ' else False

    ''' __is_valid()
    Verifica si el numero "number" es válido en la posición
    s = (i, j)
    '''

    def __is_valid(self, s: tuple, number: int) -> bool:
        number = str(number)

        # Verifica la FILA de la posición s = (i, j)
        for j in range(len(self.__board[0])):
            if number == self.__board[s[0]][j] and j != s[1]:
                return False

        # Verifica la COLUMNA de la posición s = (s, j)
        for i in range(len(self.__board)):
            if number == self.__board[i][s[1]] and i != s[0]:
                return False

        # Verifica la REGIÓN de 3x3
        i_label = s[0] // 3
        j_label = s[1] // 3
        for ii in range(len(self.__board)):
            for jj in range(len(self.__board[0])):
                if (ii // 3 == i_label and jj // 3 == j_label) and \
                        number == self.__board[ii][jj] and (ii, jj) != s:
                    return False

        return True

    ''' __next_step()
    Avanza a la siguiente posición del tablero. Primero por COLUMNAS
    luego por FILA
    '''

    def __next_step(self, s: tuple) -> tuple:
        i = s[0] if s[1] < self.__col_len-1 else s[0]+1
        j = s[1]+1 if s[1] < self.__col_len-1 else 0

        return (i, j)

    ''' __copy_board()
    Una vez completada la tabla self.__board se copia a
    self.__maked_board para no perder la tabla
    '''

    def __copy_board(self):
        for row in self.__board:
            self.__maked_board.append(row.copy())

    ''' __backtracking()
    Es el algoritmo de Backtracking para completar la tabla
    de sudoku
    '''

    def __backtracking(self, s: tuple) -> bool:
        if s == (self.__row_len, self.__col_len-1):
            go_on = True
        else:
            go_on = False

        number = 1
        while number <= self.__col_len and go_on == False:
            if self.__is_empty(s):
                self.__board[s[0]][s[1]] = str(number)

                if self.__is_valid(s, number):

                    if s == (self.__row_len-1, self.__col_len-1):
                        self.__copy_board()
                        go_on = True

                    else:
                        go_on = self.__backtracking(self.__next_step(s))

                self.__board[s[0]][s[1]] = ' '
                number += 1
            else:
                if s == (self.__row_len-1, self.__col_len-1):
                    self.__copy_board()
                    go_on = True

                else:
                    s = self.__next_step(s)

        return go_on

    def solve(self):
        return self.__backtracking((0, 0))


class SamuraiSudoku:
    def __init__(self, boards: dict):
        self.__boards = boards
        self.__sequence_list = self.__listing_sequence()
        self.__sudokus = []
        self.__samurai_sudoku = [[' ' for i in range(21)] for i in range(21)]

    def get_boards(self) -> dict:
        return self.__boards

    '''
    Recorre una tabla de sudoku y retorna True sí tiene números
    pista o retorna False si está vacía.
    '''

    def __traverse_board(self, board: list) -> bool:
        row_len = len(board)
        col_len = len(board[0])

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] != ' ':
                    return True

        return False

    '''
    Retorna el número de la primera tabla a resolver.
    '''

    def __verify_boards(self) -> int:
        with_numbers = []
        for i in range(5):
            if self.__traverse_board(self.__boards[i]):
                with_numbers.append(i)

        boards_len = len(with_numbers)
        if boards_len == 5:
            return with_numbers[4]
        elif boards_len >= 1 and boards_len <= 4:
            return with_numbers[0]
        else:
            return 4

    '''
    Genera una lista con la secuencia de tablas a resolver.
    '''

    def __listing_sequence(self) -> list:
        board_to_start = self.__verify_boards()

        sequencing_list = [board_to_start]
        if board_to_start != 4:
            sequencing_list.append(4)

        for i in range(4):
            if i != board_to_start:
                sequencing_list.append(i)

        print(sequencing_list)
        return sequencing_list

    '''
    Copia de tabla "b1" a la tabla "b2" la región específica "region_copy"
    '''

    def __copy_region(self, b1: list, b2: list, region_copy: int):
        row_len = len(b1)
        col_len = len(b1[0])

        for i in range(row_len):
            for j in range(col_len):
                if region_copy == 0 and (i // 3 == 0 and j // 3 == 0):
                    b2[i+6][j+6] = b1[i][j]
                elif region_copy == 1 and (i // 3 == 0 and j // 3 == 2):
                    b2[i+6][j-6] = b1[i][j]
                elif region_copy == 2 and (i // 3 == 2 and j // 3 == 0):
                    b2[i-6][j+6] = b1[i][j]
                elif region_copy == 3 and (i // 3 == 2 and j // 3 == 2):
                    b2[i-6][j-6] = b1[i][j]

    def __copy(self, b1, b2, region):
        board_to_copy = self.__sudokus[b1].get_maked_board()
        self.__copy_region(
            board_to_copy,
            self.__boards[b2],
            region
        )

    def __choose_board(self, i):
        inverted_regions = {
            0: 3,
            1: 2,
            2: 1,
            3: 0
        }

        if self.__sequence_list[0] == 4 and self.__sequence_list[i] != 4:
            self.__copy(
                0,
                self.__sequence_list[i],
                self.__sequence_list[i]
            )
        else:
            if self.__sequence_list[i] == 4 and i != 0:
                self.__copy(
                    0,
                    self.__sequence_list[1],
                    inverted_regions[self.__sequence_list[i-1]]
                )

            elif self.__sequence_list[i] != 4 and i != 0:
                self.__copy(
                    1,
                    self.__sequence_list[i],
                    self.__sequence_list[i]
                )

    def __sort_boards(self):
        sudokus_dict = {}
        for i in range(len(self.__sequence_list)):
            sudokus_dict[self.__sequence_list[i]] = self.__sudokus[i]

        self.__sudokus.clear()
        for i in range(len(sudokus_dict)):
            self.__sudokus.append(sudokus_dict[i])

    def __print_table(self):
        for i in range(21):
            print(
                '-------------------------------------------' +
                '------------------------------------------'
            )
            for j in range(21):
                if self.__samurai_sudoku[i][j] != ' ':
                    print('| {} '.format(self.__samurai_sudoku[i][j]), end='')
                else:
                    print('    ', end='')
            print('|')
        print(
            '-------------------------------------------' +
            '------------------------------------------'
        )

    def __join_boards(self):
        start = {  # index to star
            0: ((0, 9), (0, 9)),
            1: ((0, 9), (12, 21)),
            2: ((12, 21), (0, 9)),
            3: ((12, 21), (12, 21)),
            4: ((6, 15), (6, 15))
        }

        for k in range(len(self.__sudokus)):
            y_label = 0
            board = self.__sudokus[k].get_maked_board()
            for i in range(start[k][0][0], start[k][0][1]):
                x_label = 0
                for j in range(start[k][1][0], start[k][1][1]):
                    self.__samurai_sudoku[i][j] = board[y_label][x_label]
                    x_label += 1
                y_label += 1

    def __make_boards(self):
        for i in range(5):
            self.__choose_board(i)

            board = Sudoku(self.__boards[self.__sequence_list[i]])
            self.__sudokus.append(board)
            self.__sudokus[i].solve()

        self.__sort_boards()
        self.__join_boards()
        self.__print_table()

    def solve(self):
        self.__make_boards()
