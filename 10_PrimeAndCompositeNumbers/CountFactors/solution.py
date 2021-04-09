## https://app.codility.com/demo/results/trainingPSFN8V-VMJ/

def solution(N):
    # write your code in Python 3.6
    i = 1
    result = 0
    
    while i**2<N:
        if N%i==0:
            result += 2
        i += 1

    if i**2==N:
        result += 1
    
    return result