board = [['1', ' ', ' ', ' ', ' ', ' ', ' ', '9', ' '],
         ['8', '4', ' ', ' ', ' ', '2', ' ', ' ', ' '],
         [' ', ' ', ' ', '3', '8', ' ', '2', ' ', ' '],
         [' ', ' ', ' ', '9', ' ', ' ', '8', '5', '3'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['5', '3', '8', ' ', ' ', '6', ' ', ' ', ' '],
         [' ', ' ', '1', ' ', '7', '9', ' ', ' ', ' '],
         [' ', ' ', ' ', '5', ' ', ' ', ' ', '6', '7'],
         [' ', '2', ' ', ' ', ' ', ' ', ' ', ' ', '9']]

samurai = {
    0: [[' ', ' ', '3', ' ', ' ', ' ', '6', ' ', '5'],
        ['5', ' ', ' ', ' ', ' ', ' ', '4', ' ', '2'],
        [' ', ' ', '8', ' ', ' ', '4', ' ', ' ', ' '],
        [' ', '5', ' ', '4', ' ', '3', ' ', ' ', ' '],
        [' ', '6', ' ', '5', ' ', '7', ' ', ' ', ' '],
        ['7', ' ', ' ', '2', ' ', ' ', '5', ' ', '4'],
        [' ', '8', ' ', '7', ' ', '5', ' ', ' ', '6'],
        [' ', ' ', ' ', ' ', '8', '6', ' ', '1', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '8', ' ', ' ']],

    1: [[' ', '4', ' ', ' ', ' ', ' ', '7', '5', ' '],
        [' ', ' ', '1', ' ', ' ', '7', ' ', ' ', '4'],
        [' ', '5', ' ', ' ', '3', ' ', ' ', '8', ' '],
        [' ', '3', ' ', ' ', ' ', '1', ' ', ' ', '2'],
        ['1', ' ', '5', ' ', ' ', ' ', ' ', '4', ' '],
        ['7', ' ', '2', '9', ' ', '8', ' ', ' ', ' '],
        ['5', ' ', ' ', '1', ' ', '3', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', '2', ' ', '8'],
        [' ', ' ', '4', ' ', ' ', '6', ' ', '7', ' ']],

    2: [[' ', '9', ' ', '7', ' ', '8', ' ', ' ', ' '],
        [' ', ' ', '4', ' ', ' ', '9', '7', '8', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', '3'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '7'],
        ['7', '1', ' ', ' ', ' ', '5', ' ', '9', ' '],
        [' ', ' ', '8', ' ', ' ', '3', '6', ' ', ' '],
        ['2', ' ', ' ', ' ', ' ', ' ', '4', ' ', '6'],
        ['5', '7', '3', '6', ' ', ' ', ' ', ' ', '8'],
        [' ', ' ', ' ', '3', ' ', ' ', ' ', '7', ' ']],

    3: [[' ', ' ', '9', '2', ' ', ' ', '4', ' ', ' '],
        [' ', ' ', '1', ' ', ' ', ' ', '6', ' ', ' '],
        [' ', '5', '6', ' ', '3', ' ', ' ', ' ', ' '],
        ['9', ' ', '3', ' ', '1', '2', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', '3', '7', ' ', ' '],
        ['5', ' ', '4', ' ', '7', ' ', ' ', '8', '2'],
        [' ', ' ', ' ', '7', ' ', '6', '9', ' ', '4'],
        [' ', '3', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '7', ' ', '4', ' ', '8', ' ', ' ']],

    4: [[' ', ' ', '6', ' ', ' ', ' ', '5', ' ', ' '],
        [' ', '1', ' ', ' ', ' ', '8', ' ', ' ', ' '],
        ['8', ' ', '7', '3', ' ', ' ', ' ', ' ', '4'],
        [' ', '3', '2', '9', ' ', ' ', '8', ' ', ' '],
        [' ', '7', ' ', ' ', '6', ' ', ' ', '9', ' '],
        ['6', ' ', ' ', ' ', ' ', '4', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '5', ' ', ' ', ' ', '9'],
        ['7', '8', ' ', ' ', ' ', '9', ' ', ' ', '1'],
        [' ', '2', '3', '4', '8', ' ', ' ', '5', '6']]
}

T3 = {
    0: [['1', '6', '2', '3', '4', '5', '7', '8', '9'],
        ['8', '7', '3', ' ', ' ', ' ', ' ', ' ', ' '],
        ['9', '5', '4', ' ', ' ', ' ', ' ', ' ', ' '],
        ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    1: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    2: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    3: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    4: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
}


t4 = {
    0: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    1: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    2: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    3: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],

    4: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
}
