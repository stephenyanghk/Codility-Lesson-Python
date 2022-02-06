## https://app.codility.com/demo/results/trainingV3A2CZ-RHB/

def solution(A):
    # write your code in Python 3.6
    if len(A)<2:
        return 0

    buyat, sellat = A[0], A[0]
    max_profit = 0
    
    for p in A:
        if p<buyat:
            buyat, sellat = p, p
        elif p>sellat:
            sellat = p
            max_profit = max(max_profit, sellat-buyat)
            
    return max_profit
