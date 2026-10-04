#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)]
    
    lastAnswer = 0
    result = []
    
    for q in queries:
        typ = q[0]
        x = q[1]
        y = q[2]
        
        index = (x ^ lastAnswer) % n
        
        if typ == 1:
            arr[index].append(y)
        
        elif typ == 2:
            pos = y % len(arr[index])
            lastAnswer = arr[index][pos]
            result.append(lastAnswer)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
