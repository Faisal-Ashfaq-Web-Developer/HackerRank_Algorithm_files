#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'simpleArraySum' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.

def simpleArraySum(arr):
    total = sum(arr)
    return total
    # Write your code here


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        ar_count = int(input().strip())

        ar = list(map(int, input().rstrip().split()))

        result = simpleArraySum(ar)

        fptr.write(str(result) + '\n')
