#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    # input always a list of lists that have length = 6

    # get every hourglass - we can start with getting every 3x3 grid
    grids = []

    #input is always 6x6 grid, so there will be no more 3x3 grids after the 4th row
    for rowIndex in range(4):
        for columnIndex in range(4):

            grid = []

            row = arr[rowIndex]
            row2 = arr[rowIndex + 1]
            row3 = arr[rowIndex + 2]

            grid.append(row[columnIndex:columnIndex + 3])
            grid.append(row2[columnIndex:columnIndex + 3])
            grid.append(row3[columnIndex:columnIndex + 3])

            grids.append(grid)

    # get hourglass sums for each grid (sum of every in number in grid except for grid[1][0] and grid[1][2])
    sums = []
    for grid in grids:
        thisSum = sum(grid[0]) + grid[1][1] + sum(grid[2])
        sums.append(thisSum)

    
    # finally, get the largest sum
    return max(sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
