## https://app.codility.com/demo/results/trainingKPSVAR-PDR/

def solution(S):
    # write your code in Python 3.6
    st = []
    for c in S:
        if c=='(':
            st.append(c)
        else:
            if len(st)>0 and st[-1]=='(':
                st.pop()
            else:
                return 0
    return 0 if len(st)>0 else 1