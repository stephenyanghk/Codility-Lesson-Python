## https://app.codility.com/demo/results/training7M926W-2RX/

def solution(A):
    # write your code in Python 3.6

    lower = [0]*len(A)
    upper = [0]*len(A)

    for i in range(len(A)):
        lower[i] = i - A[i]
        upper[i] = i + A[i]

    lower.sort()
    upper.sort()

    intersection = 0
    j = 0

    for i in range(len(A)):
        while j<len(A) and upper[i]>=lower[j]:
            intersection += j
            intersection -= i
            j += 1

    return intersection if intersection<=10000000 else -1