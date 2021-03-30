# https://app.codility.com/demo/results/trainingFAPSAW-MEV/

def solution(A):
    # write your code in Python 3.6
    left_sum = A[0]
    right_sum = sum(A[1:])
    min_diff = abs(left_sum-right_sum)

    for i in range(1, len(A)-1):
        left_sum += A[i]
        right_sum -= A[i]
        min_diff = min(min_diff, abs(left_sum-right_sum))

    return min_diff