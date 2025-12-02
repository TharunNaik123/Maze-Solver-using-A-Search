
#  **2. maze.py**
python
# maze.py

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, row, col):
        return (0 <= row < self.rows and
                0 <= col < self.cols and
                self.grid[row][col] == 0)
