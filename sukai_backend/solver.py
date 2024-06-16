import numpy as np
from typing import Optional, Tuple


class Sudoku:
    """
    Class representing a Sudoku puzzle.
    
    Attributes:
    - grid (np.ndarray): 9x9 NumPy array representing the Sudoku grid.
    - solved_grid (Optional[np.ndarray]): A 9x9 NumPy array representing the solved Sudoku grid, or None if unsolvable or not yet computed.
    - rows (list[set[int]]): List of sets to track numbers in each row.
    - cols (list[set[int]]): List of sets to track numbers in each column.
    - subgrids (list[set[int]]): List of sets to track numbers in each 3x3 subgrid.
    """
    

    def __init__(self, grid: np.ndarray):
        """
        Initialize a Sudoku puzzle with the given grid.
        
        Args:
        - grid (np.ndarray): 9x9 NumPy array representing the Sudoku grid.
        """
        self.grid: np.ndarray = grid
        self.solved_grid: Optional[np.ndarray] = None
        self.rows: list[set[int]] = [set() for _ in range(9)]
        self.cols: list[set[int]] = [set() for _ in range(9)]
        self.subgrids: list[set[int]] = [set() for _ in range(9)]

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
        - grid (np.ndarray): A 9x9 NumPy array representing the Sudoku grid to be solved.

        Returns:
        - bool: True if the puzzle is solved, False otherwise.
        """
        empty_cell = self.find_empty_cell(grid)
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
        Check if the placement of 'num' at position ('row', 'col') is valid.

        Args:
        - row (int): Row index.
        - col (int): Column index.
        - num (int): Number to be placed.

        Returns:
        - bool: True if the placement is valid, False otherwise.
        """
        if num in self.rows[row]:
            return False
        if num in self.cols[col]:
            return False
        if num in self.subgrids[(row // 3) * 3 + (col // 3)]:
            return False
        
        return True

        
    def find_empty_cell(self, grid: np.ndarray) -> Optional[Tuple[int, int]]:
        """
        Find the next empty cell on the Sudoku grid.

        Args:
        - grid (np.ndarray): A 9x9 NumPy array representing the Sudoku grid.
        
        Returns:
        - Optional[Tuple[int, int]]: A tuple containing the coordinates (row, col) of the empty cell.
        """
        for row in range(9):
            for col in range(9):
                if grid[row, col] == 0:
                    return (row, col)

        return None