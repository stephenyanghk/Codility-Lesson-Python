## https://app.codility.com/demo/results/trainingPSNHUS-SR3/

def solution(S, P, Q):
    # write your code in Python 3.6
    result = [0]*len(P)

    A_list = [0]*(len(S)+1)
    C_list = [0]*(len(S)+1)
    G_list = [0]*(len(S)+1)
    T_list = [0]*(len(S)+1)

    for i in range(len(S)):
        if S[i]=='A':
            A_list[i+1] = A_list[i] + 1
            C_list[i+1] = C_list[i]
            G_list[i+1] = G_list[i]
            T_list[i+1] = T_list[i]
        elif S[i]=='C':
            A_list[i+1] = A_list[i]
            C_list[i+1] = C_list[i] + 1
            G_list[i+1] = G_list[i]
            T_list[i+1] = T_list[i]
        elif S[i]=='G':
            A_list[i+1] = A_list[i]
            C_list[i+1] = C_list[i]
            G_list[i+1] = G_list[i] + 1
            T_list[i+1] = T_list[i]
        elif S[i]=='T':
            A_list[i+1] = A_list[i]
            C_list[i+1] = C_list[i]
            G_list[i+1] = G_list[i]
            T_list[i+1] = T_list[i] + 1

    for i in range(len(P)):
        start = P[i]
        end = Q[i]

        if A_list[start]<A_list[end+1]:
            result[i] = 1
        elif C_list[start]<C_list[end+1]:
            result[i] = 2
        elif G_list[start]<G_list[end+1]:
            result[i] = 3
        else:
            result[i] = 4

    return result