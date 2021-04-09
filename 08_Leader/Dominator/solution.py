## https://app.codility.com/demo/results/training79493P-NX2/

def solution(A):
    # write your code in Python 3.6
    from collections import defaultdict

    n = len(A)
    threshold = n/2
    counter = defaultdict(int)
    for i in A:
        counter[i] += 1
        if counter[i]>threshold:
            return A.index(i)

    return -1