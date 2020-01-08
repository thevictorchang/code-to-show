#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    currentLevel = 0
    levelAtLastStep = 0
    valleysCount = 0

    # basically, for each step we keep track of the altitude/level we were at on the *last* step - if the step we're making puts us back to sea level AND our last step was below sea level,
    # then we must've just went through a valley.

    for stepIndex in range(len(s)):

        if (s[stepIndex] == 'U'):
            currentLevel += 1
        if (s[stepIndex] == 'D'):
            currentLevel -= 1
        
        if ((currentLevel == 0) and (levelAtLastStep < 0)):
            valleysCount += 1
                
        levelAtLastStep = currentLevel

    return valleysCount

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
