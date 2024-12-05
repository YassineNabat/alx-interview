#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    n = len(grid)
    for i in range(n):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == n - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
