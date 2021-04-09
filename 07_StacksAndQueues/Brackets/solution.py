## https://app.codility.com/demo/results/training3DWH5D-KEV/

def solution(S):
    # write your code in Python 3.6
    st = []

    for c in S:
        if c in {'{', '[', '('} :
            st.append(c)
        elif c=='}':
            if len(st)>0 and st[-1]=='{':
                st.pop()
            else:
                return 0
        elif c==']':
            if len(st)>0 and st[-1]=='[':
                st.pop()
            else:
                return 0
        elif c==')':
            if len(st)>0 and st[-1]=='(':
                st.pop()
            else:
                return 0

    return 0 if len(st)>0 else 1