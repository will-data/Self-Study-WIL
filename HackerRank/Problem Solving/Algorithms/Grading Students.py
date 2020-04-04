#!/bin/python3
import os
import sys


# Complete the gradingStudents function below.
#
def gradingStudents(grade):
    if grade < 38 or grade % 5 < 3:
        return grade
    else:
        return grade + 5 - grade % 5


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        grade = int(input())
        print(gradingStudents(grade))
