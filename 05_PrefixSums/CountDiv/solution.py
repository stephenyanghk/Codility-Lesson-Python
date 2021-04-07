## https://app.codility.com/demo/results/training85WVQX-W6H/

def solution(A, B, K):
    # write your code in Python 3.6
    result = int(B/K) - int(A/K)
    return result if A%K!=0 else result+1