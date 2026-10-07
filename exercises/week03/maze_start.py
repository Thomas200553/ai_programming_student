"""
Oefening 1: Maze met DFS
=========================
Implementeer DFS om een weg door het maze te vinden.
"""
import numpy as np


class Maze:
    def __init__(self, size, start, end, walls):
        self.size = size
        self.start = start
        self.end = end
        self.maze = np.zeros(size, dtype=str)
        self.maze[:, :] = '.'
        self.maze[start] = 'S'
        self.maze[end] = 'E'
        for wall in walls:
            self.maze[wall] = '#'

    def valid_moves(self, current):
        # TODO: geef lijst van (rij,kolom)-coördinaten die geldig zijn
        i, j = current
        above = (i - 1, j)
        below = (i + 1, j)
        left = (i, j - 1)
        right = (i, j + 1)

        candidates = [above, below, left, right]

        result = []
        for r, c in candidates:
            if (0 <= r < self.size[0]) and (0 <= c < self.size[1]) and (self.maze[r, c] != "#"):
                result.append((r, c))
        return result



    def extract_path(self, stack):
        # TODO: haal het pad uit de stack van start tot end
        return list(stack)

    def print_maze(self):
        for row in self.maze:
            print(' '.join(row))


def find_path(maze):
    # TODO: implementeer DFS met een stack
    visited = {maze.start}
    stack = [maze.start]

    while stack:
        current = stack[-1]

        if current == maze.end:
            path = maze.extract_path(stack)
            return path, len(path) - 1

        next_position = None

        for neighbor in maze.valid_moves(current):
            if neighbor not in visited:
                next_position = neighbor
                break

        if next_position is not None:
            stack.append(next_position)
            visited.add(next_position)
        else:
            stack.pop()

    return None, 0


if __name__ == "__main__":
    maze_size = (10, 10)
    start_point = (0, 0)
    end_point = (9, 9)
    walls = [(2, 1), (2, 2), (2, 3), (4, 6), (6, 6), (7, 6), (8, 6),
             (4, 7), (4, 8), (2, 2), (5, 2), (6, 2), (4, 2), (3, 2),
             (8, 0), (9, 6), (1, 8), (2, 8), (6, 9), (7, 9),
             (3, 6), (3, 7), (4, 1), (5, 1)]

    my_maze = Maze(maze_size, start_point, end_point, walls)
    pad, stappen = find_path(my_maze)

    my_maze.print_maze()
    print("Pad:", pad)
    print("Stappen:", stappen)