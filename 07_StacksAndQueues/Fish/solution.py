## https://app.codility.com/demo/results/trainingZK4AJG-CC2/

def solution(A, B):
    # write your code in Python 3.6

    st = []
    alive = 0

    for i in range(len(A)):
        size = A[i]
        updown = B[i]
        if updown==1:
            st.append(size)
        else:
            while len(st)>0 and st[-1]<size:
                st.pop()

            if len(st)==0:
                alive += 1

    alive += len(st)

    return alive