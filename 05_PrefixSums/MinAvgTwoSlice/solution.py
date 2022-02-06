## https://app.codility.com/demo/results/trainingC2F8N2-2TY/

def solution(A):
    # write your code in Python 3.6
    if len(A)==2:
        return 0

    minSlice2 = A[0] + A[1]
    minIndex2 = 0

    minSlice3 = A[0] + A[1] + A[2]
    minIndex3 = 0

    for i in range(2, len(A)):
        slice2 = A[i-1] + A[i]
        if slice2<minSlice2:
            minSlice2 = slice2
            minIndex2 = i - 1

        slice3 = A[i-2] + A[i-1] + A[i]
        if slice3<minSlice3:
            minSlice3 = slice3
            minIndex3 = i - 2

    minSlice2 *= 3
    minSlice3 *= 2

    if minSlice2==minSlice3:
        return min(minIndex2, minIndex3)

    return minIndex2 if minSlice2<minSlice3 else minIndex3
