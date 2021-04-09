## https://app.codility.com/demo/results/trainingC8QXK7-5BP/

def solution(A):
    # write your code in Python 3.6
    max_sum = A[0]
    curr_max = A[0]
    for i in range(1, len(A)):
        curr_max = max(A[i], curr_max+A[i])
        max_sum = max(max_sum, curr_max)
    return max_sum