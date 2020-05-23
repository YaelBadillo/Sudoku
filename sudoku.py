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

    def __assign_color(self, s) -> str:
        ''' __assign_color()
        Asinga el color a un numero dependiendo su posición s = (i, j).
        '''

        i_key = s[0] // 3
        j_key = s[1] // 3

        return SUDOKU_COLORS[str(i_key) + str(j_key)]

    def print_board(self):
        ''' print_board()
        Imprime la tabla inicial, con formato.
        '''

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

    def print_maked_board(self):
        ''' print_maked_board()
        Imprime la tabla llena, con formato.
        '''

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

    def __is_empty(self, s: tuple) -> bool:
        ''' ___is_empty()
        Verifica si la posición s = (i, j) del tablero self.__board,
        está vacía.
        '''

        return True if self.__board[s[0]][s[1]] == ' ' else False

    def __is_valid(self, s: tuple, number: int) -> bool:
        ''' __is_valid()
        Verifica si el numero "number" es válido en la posición
        s = (i, j).
        '''

        number = str(number)

        # Verifica la FILA de la posición s = (i, j)
        for j in range(len(self.__board[0])):
            if number == self.__board[s[0]][j] and j != s[1]:
                return False

        # Verifica la COLUMNA de la posición s = (s, j)
        for i in range(len(self.__board)):
            if number == self.__board[i][s[1]] and i != s[0]:
                return False

        # Verifica la REGIÓN de 3x3.
        i_label = s[0] // 3
        j_label = s[1] // 3
        for ii in range(len(self.__board)):
            for jj in range(len(self.__board[0])):
                if (ii // 3 == i_label and jj // 3 == j_label) and \
                        number == self.__board[ii][jj] and (ii, jj) != s:
                    return False

        return True

    def __next_step(self, s: tuple) -> tuple:
        ''' __next_step()
        Avanza a la siguiente posición del tablero. Primero por COLUMNAS
        luego por FILA.
        '''

        i = s[0] if s[1] < self.__col_len-1 else s[0]+1
        j = s[1]+1 if s[1] < self.__col_len-1 else 0

        return (i, j)

    def __copy_board(self):
        ''' __copy_board()
        Una vez completada la tabla self.__board se copia a
        self.__maked_board para no perder la tabla.
        '''

        for row in self.__board:
            self.__maked_board.append(row.copy())

    def __backtracking(self, s: tuple) -> bool:
        ''' __backtracking()
        Es el algoritmo de Backtracking para completar la tabla
        de sudoku.
        '''

        # Retorna True si los indices "s = (i, j)" se encuentran
        # en la última posición de self.__board.
        if s == (self.__row_len, self.__col_len-1):
            go_on = True
        else:
            go_on = False

        number = 1
        # Recorre todos los números posibles del 1 al 9.
        while number <= self.__col_len and go_on == False:
            # Retorna True si la posición actual "s = (i, j)" se
            # encuentra vacía.
            if self.__is_empty(s):
                # Asigna el numero "number" en la posición actual "s"
                # en la tabla "self.__board".
                self.__board[s[0]][s[1]] = str(number)

                # Retorna True sí el número "number" es válido en la
                # posicion "s = (i, j)" de la tabla.
                if self.__is_valid(s, number):
                    # Verifica si los indices ya llegaron a su última
                    # posición. Copiará la tabla y retornará
                    # True.
                    if s == (self.__row_len-1, self.__col_len-1):
                        self.__copy_board()  # Copia la tabla para no perder avances
                        go_on = True        # Retorna True para terminar el Backtracking

                    else:
                        # Si la tabla aun no se llena, vuelve a llamarse la función
                        # para la siguiente posición "s = (i, j)" del tablero.
                        go_on = self.__backtracking(self.__next_step(s))

                # Sí el número no es válido se vuelve a vaciar la posición.
                self.__board[s[0]][s[1]] = ' '
                number += 1  # Siguiente número en caso de no ser válido el actual
            else:
                # Verifica si los indices ya llegaron a su última
                # posición. Copiará la tabla y retornará
                # True.
                if s == (self.__row_len-1, self.__col_len-1):
                    self.__copy_board()
                    go_on = True

                else:
                    # Aumenta una posición en el tablero si aun no se llega a la
                    # última posición.
                    s = self.__next_step(s)

        return go_on

    def solve(self):
        '''
        Función pública para resolver la tabla.
        '''
        return self.__backtracking((0, 0))


class SamuraiSudoku:
    def __init__(self, boards: dict):
        # Lista de tablas sin hacer.
        self.__boards = boards
        # Lista de tablas iniciales.
        self.__empty_boards = boards
        # Lista de orden de tablas a hacer.
        self.__sequence_list = self.__listing_sequence()
        # Lista de objetos Sudoku de cada tabla.
        self.__sudokus = []
        # Tabla Final de 21x21.
        self.__samurai_sudoku = [[' ' for i in range(21)] for i in range(21)]

    def get_boards(self) -> dict:
        return self.__boards

    def __traverse_board(self, board: list) -> bool:
        '''
        Recorre una tabla de sudoku y retorna True sí tiene números
        pista o retorna False si está vacía.
        '''

        row_len = len(board)
        col_len = len(board[0])

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] != ' ':
                    return True

        return False

    def __verify_boards(self) -> int:
        '''
        Retorna el número de la primera tabla a resolver.
        '''

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

    def __listing_sequence(self) -> list:
        '''
        Genera una lista con la secuencia de tablas a resolver.
        '''

        board_to_start = self.__verify_boards()

        sequencing_list = [board_to_start]
        if board_to_start != 4:
            sequencing_list.append(4)

        for i in range(4):
            if i != board_to_start:
                sequencing_list.append(i)

        return sequencing_list

    def __copy_region(self, b1: list, b2: list, region_copy: int):
        '''
        Copia de tabla "b1" a la tabla "b2" la región específica "region_copy".
        '''

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

    def __copy(self, board_1, board_2, region):
        '''
        Copia la región de la tabla "board_1" a la tabla "board_2".
        '''

        board_to_copy = self.__sudokus[board_1].get_maked_board()
        self.__copy_region(
            board_to_copy,
            self.__boards[board_2],
            region
        )

    def __choose_board(self, i):
        '''
        Elige la región a copiar de tabla 1 a tabla 2 dependiendo cual sea
        la tabla 1 (tabla llena).

        '''

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

    def __make_boards(self):
        '''
        Llena todas las tablas y las guarfa en self.__sudokus.
        '''
        for i in range(5):
            self.__choose_board(i)

            board = Sudoku(self.__boards[self.__sequence_list[i]])
            self.__sudokus.append(board)
            self.__sudokus[i].solve()

    def __sort_boards(self):
        '''
        Ordenas las tablas dejando en última posición a la 
        tabla central.
        '''
        self.__make_boards()

        sudokus_dict = {}
        for i in range(len(self.__sequence_list)):
            sudokus_dict[self.__sequence_list[i]] = self.__sudokus[i]

        self.__sudokus.clear()
        for i in range(len(sudokus_dict)):
            self.__sudokus.append(sudokus_dict[i])

    def __join_boards(self):
        '''
        Une las 5 tablas en una única tabla "self.__samurai_sudoku" de 21x21.
        '''

        # Primero las ordenamos
        self.__sort_boards()

        # Primera posición para cada tabla en la "self.__samurai_sudoku".
        start = {
            0: (0, 0),          # TABLA 0
            1: (0, 12),         # TABLA 1
            2: (12, 0),         # TABLA 2
            3: (12, 12),        # TABLA 3
            4: (6, 6)           # TABLA 4
        }

        # Recorremos todas las tablas
        for number in range(len(self.__sudokus)):
            board = self.__sudokus[number].get_maked_board()

            # Posición inicial de fila en tabla de 21x21
            ii = start[number][0]
            for i in range(9):
                # Posición inicial de columna en tabla de 21x21
                jj = start[number][1]
                for j in range(9):
                    self.__samurai_sudoku[ii][jj] = board[i][j]
                    jj += 1
                ii += 1

    def __assign_color(self, i, j):
        '''
        Asigna un color a cada región al imprimir la tabla FINAL 
        dependiendo la región.
        '''

        i_key = i // 3
        j_key = j // 3
        region = str(i_key) + str(j_key)

        color_keys = list(SAMURAI_COLORS)
        for key in color_keys:
            if region in key:
                return SAMURAI_COLORS[key]

        return -1

    def print_maked_table(self):
        for i in range(21):
            print(
                '-------------------------------------------' +
                '------------------------------------------'
            )
            for j in range(21):
                if self.__samurai_sudoku[i][j] != ' ':
                    print('| {}{}{} '.format(
                        self.__assign_color(i, j),
                        self.__samurai_sudoku[i][j],
                        RESET
                    ),
                        end=''
                    )

                else:
                    print('|   ', end='')
            print('|')
        print(
            '-------------------------------------------' +
            '------------------------------------------'
        )

    def solve(self):
        self.__join_boards()
