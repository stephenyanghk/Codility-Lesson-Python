# https://app.codility.com/demo/results/trainingDAZZ8W-JYT/

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    calculated_sum = (1+n+1)*(n+1)/2
    return int(calculated_sum-sum(A))