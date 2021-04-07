## https://app.codility.com/demo/results/trainingKMN5P8-4FC/

def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(2, len(A)):
        if A[i-2]+A[i-1]>A[i]:
            return 1
    return 0