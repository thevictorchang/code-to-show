#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    # start with empty list of unpaired socks (we haven't started looking through them yet!)
    unpairedSocks = []
    pairs = 0

    # for each sock, if we've already seen it and it is NOT part of a pair (i.e. in unpairedSocks), then remove it from unpairedSocks (pair it up with the one we're "holding")
    # and add one to the count of pairs, otherwise put it in the list of unpaired socks
    for sock in ar:
        if (sock in unpairedSocks):
            unpairedSocks.remove(sock)
            pairs += 1
        else:
            unpairedSocks.append(sock)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
