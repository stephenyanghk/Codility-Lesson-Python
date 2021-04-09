## https://app.codility.com/demo/results/training2UNWSF-7XF/

def solution(A):
    # write your code in Python 3.6
    max_profit = 0
    last_min = None
    
    for i in A:
        if last_min is not None and last_min>i:
            last_min = None

        if last_min is not None and last_min<i:
            max_profit = max(max_profit, i-last_min)

        if last_min is None:
            last_min = i

    return max_profit