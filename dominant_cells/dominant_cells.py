#!/bin/python3

import os
import sys

#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as a parameter.
#

def numCells(grid):
    n = len(grid)    # Number of rows
    m = len(grid[0]) # Number of columns
    dominant_count = 0

    # Define all 8 possible directions for neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
        (0, -1),         (0, 1),      # Left, Right
        (1, -1), (1, 0), (1, 1)       # Bottom-left, Bottom, Bottom-right
    ]

    for i in range(n):
        for j in range(m):
            is_dominant = True  # Assume the cell is dominant

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m:  # Ensure within bounds
                    if grid[i][j] <= grid[ni][nj]:  # If any neighbor is greater or equal
                        is_dominant = False
                        break  # Stop checking further

            if is_dominant:
                dominant_count += 1  # Count dominant cell

    return dominant_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
