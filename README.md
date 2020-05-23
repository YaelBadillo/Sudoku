# Sudoku

El Backtracking fue la estrategia usada para resolver el éste programa.

Dependiendo de las 5 tablas: se inicia a resolver la primer tabla con números pistas. En caso de tener números pistas todas las tablas o de estar todas vacía, se inicia con la tabla cental.

Se resuelve cada tabla con el método "self.__backtracking()" de la clase "Sudoku", y se copia la region de la tabla resuelta con "self.__copy_region()" de la clase "SamuraiSudoku" para poder resolver, la siguiente tabla.