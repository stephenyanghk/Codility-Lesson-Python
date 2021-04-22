## https://app.codility.com/demo/results/trainingQA4SWG-3Y5/

from collections import Counter

def solution(A):
    # write your code in Python 3.6
    c = Counter(A)
    n = len(A)
    tracking = [n]*(2*n+1)

    for k,v in c.items():
        i = 1
        while (i*k<=2*n):
            tracking[i*k] -= v
            i += 1

    result = [0]*n

    for i in range(n):
        result[i] = tracking[A[i]]

    return result