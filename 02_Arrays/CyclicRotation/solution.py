# https://app.codility.com/demo/results/trainingYGDXNF-Y4U/

def solution(A, K):
    # write your code in Python 3.6
    result = [0] * len(A)
    for i in range(len(A)):
        result[(i+K)%len(A)] = A[i]
    return result