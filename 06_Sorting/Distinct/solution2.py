## https://app.codility.com/demo/results/trainingY5J3JX-3QW/

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    
    if n==0:
        return 0

    sorted_a = sorted(A)
    prev = sorted_a[0]

    count = 1

    for i in range(1, n):
        curr = sorted_a[i]
        if curr!=prev:
            count += 1
        prev = curr

    return count