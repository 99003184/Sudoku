SIZE = 9
matrix = [
    [6, 5, 0, 8, 7, 3, 0, 9, 0],
    [0, 0, 3, 2, 5, 0, 0, 0, 8],
    [9, 8, 0, 1, 0, 4, 3, 5, 7],
    [1, 0, 5, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 5, 0, 3],
    [5, 7, 8, 3, 0, 1, 0, 2, 6],
    [2, 0, 0, 0, 4, 8, 9, 0, 0],
    [0, 9, 0, 6, 2, 5, 0, 8, 1]
    ]


def print_sudoku():
    for a in matrix:
        print (a)


def number_unassigned(row, col):
    num_unassign = 0
    for a in range(0, SIZE):
        for b in range(0, SIZE):
            if matrix[a][b] == 0:
                row = a
                col = b
                num_unassign = 1
                z = [row, col, num_unassign]
                return z
    z = [-1, -1, num_unassign]
    return z


def is_safe(e, f, g):
    for a in range(0, SIZE):
        if matrix[f][a] == e:
            return False
    for a in range(0, SIZE):
        if matrix[a][g] == e:
            return False
    row_start = (f//3)*3
    col_start = (g//3)*3
    for a in range(row_start, row_start+3):
        for b in range(col_start, col_start+3):
            if matrix[a][b] == e:
                return False
    return True


def solve_sudoku():
    row = 0
    col = 0
    z = number_unassigned(row, col)
    if z[2] == 0:
        return True
    row = z[0]
    col = z[1]
    for a in range(1, 10):
        if is_safe(a, row, col):
            matrix[row][col] = a
            if solve_sudoku():
                return True
            matrix[row][col] = 0
    return False
if solve_sudoku():
    print_sudoku()
else:
    print("No solution")
