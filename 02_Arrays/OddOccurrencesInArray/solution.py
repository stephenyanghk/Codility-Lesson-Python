# https://app.codility.com/demo/results/training364JKE-YZ8/

def solution(A):
    # write your code in Python 3.6
    result = 0
    for i in A:
        result ^= i
    return result