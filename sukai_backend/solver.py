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


    def solve(self) -> np.ndarray:
        """
        Solve the Sudoku puzzle.
        
        Returns:
        - A 9x9 NumPy array representing the solved Sudoku grid."""
        pass


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
        
        # Check that the number is not already in the current row
        if num in self.grid[row, :]:
            return False
        
        # Check that the number is not already in the current column
        if num in self.grid[:, col]:
            return False
        
        # Check that the number is not already in the current subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        subgrid = self.grid[start_row:start_row + 3, start_col:start_col + 3]
        if num in subgrid:
            return False
        
        return True

        
    def find_empty_cell(self) -> Tuple[int, int]:
        """
        Find the next empty cell on the Sudoku grid.
        
        Returns:
        - A tuple containing the coordinates (row, col) of the empty cell."""
        pass