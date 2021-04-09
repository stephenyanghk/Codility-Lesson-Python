## https://app.codility.com/demo/results/trainingQEYYZA-GEF/

def solution(N):
    # write your code in Python 3.6
    if N==1:
        return 4

    i = 1
    min_peri = None
    while i**2<N:
        if N%i==0:
            peri = i + int(N/i)
            if min_peri is not None:
                min_peri = min(min_peri, peri)
            else:
                min_peri = peri
        i += 1

    if i**2==N:
        min_peri = min(min_peri, 2*i)

    return 2*min_peri