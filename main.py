# main.py

from maze import Maze
from astar import astar_search

def load_maze(path):
    with open(path, "r") as f:
        grid = [list(map(int, line.split())) for line in f]
    return grid

def print_maze_with_path(grid, path):
    path_set = set(path)
    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0])):
            if (r, c) in path_set:
                row += " * "
            elif grid[r][c] == 1:
                row += " # "
            else:
                row += " . "
        print(row)

def main():
    grid = load_maze("example_maze.txt")
    maze = Maze(grid)

    start = (0, 0)
    goal = (3, 4)

    path = astar_search(maze, start, goal)

    if path:
        print("\nShortest Path Found:")
        print(path)
        print("\nMaze Visualization:\n")
        print_maze_with_path(grid, path)
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
