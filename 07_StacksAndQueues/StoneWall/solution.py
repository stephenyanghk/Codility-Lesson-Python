## https://app.codility.com/demo/results/training2DP56M-BCK/

def solution(H):
    # write your code in Python 3.6
    result = 0
    st = []

    for i in H:
        while len(st)>0 and i<st[-1]:
            st.pop()

        if len(st)>0 and i==st[-1]:
            continue

        st.append(i)
        result += 1

    return result