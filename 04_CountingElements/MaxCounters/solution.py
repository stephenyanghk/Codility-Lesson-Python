## https://app.codility.com/demo/results/trainingSE6TKZ-B6U/

def solution(N, A):
    # write your code in Python 3.6
    l = [0]*N

    curr_min = 0
    curr_max = 0

    for i in A:
        if i==N+1:
            curr_min = curr_max
        else:
            idx = i-1
            l[idx] = max(l[idx], curr_min)
            l[idx] += 1
            curr_max = max(curr_max, l[idx])

    return [max(curr_min, i) for i in l]
