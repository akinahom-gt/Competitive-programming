import math
import os
import random
import re
import sys


def grading(grades):
    res = []
    for grade in grades:
        if grade>=38:
            mod5 = grade % 5   
            if mod5>=3:
                grade+= (5-mod5)
        res.append(grade)
    return res   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    gradess = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        gradess.append(grades_item)

    result = grading(gradess)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
fptr.close()
