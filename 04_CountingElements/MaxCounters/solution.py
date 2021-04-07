## https://app.codility.com/demo/results/training369SPH-4ZS/

def solution(N, A):
    # write your code in Python 3.6
    result = [0]*N

    this_min = 0
    this_max = 0

    for i in A:
        if i<=N:
            id = i-1
            if result[id]<this_min:
                result[id] = this_min
            result[id] += 1
            this_max = max(this_max, result[id])
        elif i==N+1:
            this_min = this_max

    return list(map(lambda x: this_min if x<this_min else x, result))