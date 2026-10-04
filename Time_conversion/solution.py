#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s[:8]
    ampm = s[8:]
    
    hour = int(s[:2])
    
    if ampm == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour = hour + 12
    
    return str(hour).zfill(2) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
