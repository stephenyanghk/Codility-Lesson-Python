## https://app.codility.com/demo/results/trainingF3UQKM-6C9/

def solution(A):
    # write your code in Python 3.6
    result = 0
    east_car = 0

    for i in A:
        if i==0:
            east_car +=1
        else:
            result += east_car
            if result>1000000000:
                return -1

    return result
