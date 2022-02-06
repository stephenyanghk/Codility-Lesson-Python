## https://app.codility.com/demo/results/trainingZKYGE5-VHM/

def solution(A):
    # write your code in Python 3.6
    a = sorted(A, reverse=True)
    return max(a[0]*a[1]*a[2], a[0]*a[-1]*a[-2])
