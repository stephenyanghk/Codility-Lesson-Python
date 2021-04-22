https://app.codility.com/demo/results/trainingHFXANT-UQH/

def gcd(a, b):
    if b==0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return (a*b)/gcd(a, b)

def solution(N, M):
    # write your code in Python 3.6
    return int(lcm(N, M)/M)