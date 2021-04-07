## https://app.codility.com/demo/results/trainingJTX62K-7UR/

def solution(X, A):
    # write your code in Python 3.6
    s = set(range(1, X+1))
    for i in range(len(A)):
        if A[i] in s:
            s.remove(A[i])
        if len(s)==0:
            return i
    return -1