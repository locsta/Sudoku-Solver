from pprint import pprint
import time

sudoku_to_solve = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

sudoku_processing = sudoku_to_solve.copy()
nb_unknown = 0
solved = []
for liste in sudoku_to_solve:
    nb_unknown += liste.count(0)
print(nb_unknown)

sudoku_ready = []
for liste in sudoku_processing:
    sudoku_liste = []
    for value in liste:
        if value == 0:
            sudoku_liste.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
        else:
            sudoku_liste.append(value)
    sudoku_ready.append(sudoku_liste)

def print_sudoku():
    i = j = 0
    row_to_print = ""
    while i <= 8:
        row_to_print += "|"
        while j <= 8:
            if type(sudoku_ready[i][j]) == list:
                row_to_print += "   |"
            else:
                row_to_print += " " + (str(sudoku_ready[i][j]) + " |")
                pass
            j += 1
        row_to_print += "\n"
        j = 0
        i += 1
    print(row_to_print)
    

def process_lines():
    i = j = 0
    while i <= 8:
        while j <= 8:
            if type(sudoku_ready[i][j]) == list:
                for number in sudoku_ready[i]:
                    if type(number) == int and number in sudoku_ready[i][j]:
                        sudoku_ready[i][j].remove(number)
            j += 1
        j = 0
        i += 1

def process_rows():
    column = row = 0
    while column <= 8:
        while row <= 8:
            if type(sudoku_ready[row][column]) == list:
                current_column = 0
                while current_column <= 8:
                    if type(sudoku_ready[current_column][column]) == int and sudoku_ready[current_column][column] in sudoku_ready[row][column]:
                        sudoku_ready[row][column].remove(sudoku_ready[current_column][column])
                    current_column += 1
            row += 1
        row = 0
        column += 1

def process_squares():
    col = 0
    row = 0
    col_index = 0
    row_index = 0
    while row_index < 9:
        while col_index < 9:
            while row <= 2:
                while col <= 2:
                    if type(sudoku_ready[row + row_index][col + col_index]) == list:
                        i_row = 0
                        i_col = 0
                        while i_row <= 2:
                            while i_col <= 2:
                                if type(sudoku_ready[row_index + i_row][col_index + i_col]) == int and sudoku_ready[row_index + i_row][col_index + i_col] in sudoku_ready[row + row_index][col + col_index]:
                                    sudoku_ready[row + row_index][col + col_index].remove(sudoku_ready[row_index + i_row][col_index + i_col])
                                i_col += 1
                            i_col = 0
                            i_row += 1
                    col += 1
                col = 0
                row += 1
            row = 0
            col_index += 3
        col_index = 0
        row_index += 3
            
def clr_answers():
    i = j = 0
    while i <= 8:
        while j <= 8:
            if type(sudoku_ready[i][j]) == list and len(sudoku_ready[i][j]) == 1:
                sudoku_ready[i][j] = sudoku_ready[i][j][0]
                solved.append(1)
                print_sudoku()
                print(f"Sudoku solved at {(len(solved) / nb_unknown)*100:.0f}%")
                time.sleep(.2)
            j += 1
        j = 0
        i += 1

def solve_sudoku():
    while len(solved) < nb_unknown:
        process_lines()
        clr_answers()
        process_rows()
        clr_answers()
        process_squares()
        clr_answers()
        

solve_sudoku()
# print(sudoku_ready)
pprint(sudoku_ready)



