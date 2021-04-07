## https://app.codility.com/demo/results/trainingS67WAZ-ADE/

def solution(A):
    # write your code in Python 3.6
    s = set()
    for i in A:
        s.add(i)
    return len(s)