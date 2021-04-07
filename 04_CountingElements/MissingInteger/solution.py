## https://app.codility.com/demo/results/trainingB8XMTR-HKZ/

def solution(A):
    # write your code in Python 3.6
    s = set(range(1, len(A)+2))
    for i in A:
        if i in s:
            s.remove(i)
    return min(s)