## https://app.codility.com/demo/results/training2MHSNY-VQ5/

def solution(A):
    # write your code in Python 3.6
    avg2 = sum(A[0:2])/2
    avg3 = sum(A[0:3])/3

    min_idx = 0
    min_avg = min(avg2, avg3)
    
    for i in range(1, len(A)-2):
        avg2 = sum(A[i:i+2])/2
        avg3 = sum(A[i:i+3])/3
        this_min = min(avg2, avg3)
        if min_avg>this_min:
            min_avg = this_min
            min_idx = i

    avg2 = sum(A[-2:])/2
    if min_avg>avg2:
        return len(A)-2

    return min_idx