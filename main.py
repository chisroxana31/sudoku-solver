class SudokuSolver:
    def __init__(self):
        self.SIZE = 9
        self.grid = [[0] * self.SIZE for _ in range(self.SIZE)]

    def solve_sudoku(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if self.is_safe(row, col, num):
                self.grid[row][col] = num

                if self.solve_sudoku():
                    return True

                self.grid[row][col] = 0

        return False

    def is_safe(self, row, col, num):
        return not self.used_in_row(row, num) \
               and not self.used_in_col(col, num) \
               and not self.used_in_box(row - row % 3, col - col % 3, num)

    def used_in_row(self, row, num):
        return num in self.grid[row]

    def used_in_col(self, col, num):
        for i in range(self.SIZE):
            if self.grid[i][col] == num:
                return True
        return False

    def used_in_box(self, box_start_row, box_start_col, num):
        for i in range(3):
            for j in range(3):
                if self.grid[i + box_start_row][j + box_start_col] == num:
                    return True
        return False

    def find_empty_cell(self):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def read_matrix_from_file(self, filename):
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                values = line.split()
                for j, value in enumerate(values):
                    if value == 'x':
                        self.grid[i][j] = 0
                    else:
                        self.grid[i][j] = int(value)

    def print_grid(self):
        for row in self.grid:
            print(' '.join(map(str, row)))


if __name__ == "__main__":
    sudoku_solver = SudokuSolver()
    sudoku_solver.read_matrix_from_file("matrix.txt")

    print("Original Sudoku:")
    sudoku_solver.print_grid()

    if sudoku_solver.solve_sudoku():
        print("\nSolved Sudoku:")
        sudoku_solver.print_grid()
    else:
        print("\nNo solution exists.")
