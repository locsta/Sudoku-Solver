from pprint import pprint
import time


class Sudoku():
    """This class aims to solve sudokus, it takes an unsolved sudoku stored as a list of lists (9 * 9) with 0 as missing values
    """
    def __init__(self, sudoku_to_solve=[]):
        if not sudoku_to_solve:
            self.sudoku_to_solve = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        else:
            self.sudoku_to_solve = sudoku_to_solve
        self.sudoku_processing = self.sudoku_to_solve.copy()
        self.nb_unknown = sum([l.count(0) for l in self.sudoku_to_solve])
        self.solved = []
        print(f"The sudoku contains {self.nb_unknown} missing values")
        self.sudoku_ready = []

    def __preprocessing(self):
        for liste in self.sudoku_processing:
            sudoku_liste = []
            for value in liste:
                if value == 0:
                    sudoku_liste.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
                else:
                    sudoku_liste.append(value)
            self.sudoku_ready.append(sudoku_liste)

    def print_sudoku(self):
        i = j = 0
        row_to_print = f"{'-'*40}\n"
        while i <= 8:
            row_to_print += "|"
            while j <= 8:
                if type(self.sudoku_ready[i][j]) == list:
                    # row_to_print += "   |"
                    row_to_print += "    "
                else:
                    # row_to_print += " " + (str(self.sudoku_ready[i][j]) + " |")
                    row_to_print += " " + (str(self.sudoku_ready[i][j]) + "  ")
                    pass
                if (j + 1) % 3 == 0:
                     row_to_print += "|"
                j += 1
            row_to_print += "\n"
            if (i + 1) % 3 == 0:
                row_to_print += f"{'-'*40}\n"
            j = 0
            i += 1
        print(row_to_print)
    
    def __process_lines(self):
        i = j = 0
        while i <= 8:
            while j <= 8:
                if type(self.sudoku_ready[i][j]) == list:
                    for number in self.sudoku_ready[i]:
                        if type(number) == int and number in self.sudoku_ready[i][j]:
                            self.sudoku_ready[i][j].remove(number)
                j += 1
            j = 0
            i += 1
    def __process_rows(self):
        column = row = 0
        while column <= 8:
            while row <= 8:
                if type(self.sudoku_ready[row][column]) == list:
                    current_column = 0
                    while current_column <= 8:
                        if type(self.sudoku_ready[current_column][column]) == int and self.sudoku_ready[current_column][column] in self.sudoku_ready[row][column]:
                            self.sudoku_ready[row][column].remove(self.sudoku_ready[current_column][column])
                        current_column += 1
                row += 1
            row = 0
            column += 1

    def __process_squares(self):
        col = 0
        row = 0
        col_index = 0
        row_index = 0
        while row_index < 9:
            while col_index < 9:
                while row <= 2:
                    while col <= 2:
                        if type(self.sudoku_ready[row + row_index][col + col_index]) == list:
                            i_row = 0
                            i_col = 0
                            while i_row <= 2:
                                while i_col <= 2:
                                    if type(self.sudoku_ready[row_index + i_row][col_index + i_col]) == int and self.sudoku_ready[row_index + i_row][col_index + i_col] in self.sudoku_ready[row + row_index][col + col_index]:
                                        self.sudoku_ready[row + row_index][col + col_index].remove(self.sudoku_ready[row_index + i_row][col_index + i_col])
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
            
    def __clr_answers(self):
        i = j = 0
        while i <= 8:
            while j <= 8:
                if type(self.sudoku_ready[i][j]) == list and len(self.sudoku_ready[i][j]) == 1:
                    self.sudoku_ready[i][j] = self.sudoku_ready[i][j][0]
                    self.solved.append(1)
                    self.print_sudoku()
                    print(f"Sudoku solved at {(len(self.solved) / self.nb_unknown)*100:.0f}%")
                    time.sleep(.2)
                j += 1
            j = 0
            i += 1

    def solve_sudoku(self):
        self.__preprocessing()
        while len(self.solved) < self.nb_unknown:
            self.__process_lines()
            self.__clr_answers()
            self.__process_rows()
            self.__clr_answers()
            self.__process_squares()
            self.__clr_answers()
        self.print_sudoku()
        
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    sudoku = Sudoku()
    sudoku.solve_sudoku()