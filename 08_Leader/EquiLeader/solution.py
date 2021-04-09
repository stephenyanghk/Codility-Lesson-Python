## https://app.codility.com/demo/results/trainingT9NWZE-EYE/

def solution(A):
    # write your code in Python 3.6
    from collections import defaultdict

    lthreshold = len(A)/2
    leader = None
    
    equi_leader = 0
    leader_count = defaultdict(int)

    for i in A:
        leader_count[i] += 1
        if leader is None and leader_count[i]>lthreshold:
            leader = i

    a_count = 0
    b_count = leader_count[leader]

    for i in range(len(A)):
        if A[i]==leader:
            a_count += 1
            b_count -= 1

        leader_a = a_count > (i+1)/2 
        leader_b = b_count > (len(A)-i-1)/2

        if leader_a and leader_b:
            equi_leader += 1

    return equi_leader