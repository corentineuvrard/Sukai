import numpy as np
from typing import Tuple


class Sudoku:
    """
    Class representing a Sudoku puzzle.
    
    Attributes:
    - grid: 9x9 NumPy array representing the Sudoku grid.
    """
    

    def __init__(self, grid: np.ndarray):
        """
        Initialize a Sudoku puzzle with the given grid.
        
        Args:
        - grid: 9x9 NumPy array representing the Sudoku grid.
        """
        self.grid = grid
        self.solved_grid = None
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.subgrids = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = grid[r, c]
                if num > 0:
                    self.rows[r].add(num)
                    self.cols[c].add(num)
                    self.subgrids[(r // 3) * 3 + (c // 3)].add(num)

        self.precompute_solution()


    def precompute_solution(self) -> None:
        """
        Precompute the solution of the Sudoku problem.
        """
        self.solved_grid = self.grid.copy()
        if not self.solve(self.solved_grid):
            self.solved_grid = None


    def solve(self, grid: np.ndarray) -> bool:
        """
        Solve the Sudoku puzzle.
        
        Args:
        - A 9x9 NumPy array representing the Sudoku grid to be solved.

        Returns:
        - True: If the puzzle is solved.
        - False: If the puzzle is not solved.
        """
        empty_cell = self.find_empty_cell()
        if empty_cell is None:
            return True
        
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                grid[row, col] = num
                self.rows[row].add(num)
                self.cols[col].add(num)
                self.subgrids[(row // 3) * 3 + (col // 3)].add(num)

                if self.solve(grid):
                    return True

                # Backtrack
                grid[row, col] = 0
                self.rows[row].remove(num)
                self.cols[col].remove(num)
                self.subgrids[(row // 3) * 3 + (col // 3)].remove(num)

        return False


    def is_valid(self, row: int, col: int, num: int) -> bool:
        """
        Check if the current grid state is valid after placing 'num' at position ('row', 'col').

        Args:
        - row: Row index.
        - col: Column index.
        - num: Number to be placed.

        Returns:
        - True: If the grid state is valid.
        - False: If the grid state is not valid.
        """
        if num in self.rows[row]:
            return False
        if num in self.cols[col]:
            return False
        if num in self.subgrids[(row // 3) * 3 + (col // 3)]:
            return False
        
        return True

        
    def find_empty_cell(self) -> Tuple[int, int]:
        """
        Find the next empty cell on the Sudoku grid.
        
        Returns:
        - A tuple containing the coordinates (row, col) of the empty cell.
        """
        for row in range(9):
            for col in range(9):
                if self.grid[row, col] == 0:
                    return (row, col)
        
        return None