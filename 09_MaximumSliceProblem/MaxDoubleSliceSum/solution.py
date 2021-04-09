## https://app.codility.com/demo/results/trainingK5626N-2ZF/

def solution(A):
    # write your code in Python 3.6
    max_left = [0]*len(A)
    max_right = [0]*len(A)

    for i in range(1, len(A)):
        max_left[i] = max(0, max_left[i-1]+A[i])

    for i in range(len(A)-2, -1, -1):
        max_right[i] = max(0, max_right[i+1]+A[i])

    max_sum = 0
    for i in range(1, len(A)-1):
        curr_sum = max_left[i-1] + max_right[i+1]
        max_sum = max(max_sum, curr_sum)

    return max_sum