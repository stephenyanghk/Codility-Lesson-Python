## https://app.codility.com/demo/results/trainingHTA9WY-DMJ/

def solution(A):
    # write your code in Python 3.6
    max_profit = 0
    st = []
    
    for i in A:
        while len(st)>0 and st[-1]>i:
            st.pop()

        if len(st)>0 and st[-1]<i:
            max_profit = max(max_profit, i-st[-1])

        if len(st)==0:
            st.append(i)

    return max_profit