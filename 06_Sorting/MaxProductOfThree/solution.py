## https://app.codility.com/demo/results/trainingFJN95J-U7Y/

def solution(A):
    # write your code in Python 3.6
    A = sorted(A, reverse=True)
    p3 = lambda x, y, z: x*y*z
    results = [p3(A[0], A[1], A[2]), p3(A[0], A[-1], A[-2])]
    return max(results)