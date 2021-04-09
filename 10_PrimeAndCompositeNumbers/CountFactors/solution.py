## https://app.codility.com/demo/results/trainingZEJSAF-RTQ/

def solution(N):
    # write your code in Python 3.6
    factor = 0
    sqrt_N = int(N**0.5)

    for i in range(1, sqrt_N+1):
        if N%i==0:
            factor += 2

    if sqrt_N**2==N:
        factor -= 1

    return factor