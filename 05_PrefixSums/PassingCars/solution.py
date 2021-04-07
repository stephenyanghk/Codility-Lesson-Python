## https://app.codility.com/demo/results/trainingF3UQKM-6C9/

def solution(A):
    # write your code in Python 3.6
    result = 0
    count_factor = 0
    for i in A:
        if i==1:
            result += count_factor
        else:
            count_factor += 1
    return result if result<=1000000000 else -1