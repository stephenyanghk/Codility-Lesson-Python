## https://app.codility.com/demo/results/training98U3UD-JNC/

def solution(N):
    # write your code in Python 3.6
    s = set(range(1, len(N)+1))
    for i in N:
        if i not in s:
            return 0
        else:
            s.remove(i)
    return 1 if len(s)==0 else 0