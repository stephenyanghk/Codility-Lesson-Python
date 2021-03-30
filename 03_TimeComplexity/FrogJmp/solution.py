# https://app.codility.com/demo/results/trainingWFKAEN-TY9/

import math

def solution(X, Y, D):
    # write your code in Python 3.6
    d = Y-X
    return math.ceil(d/D)