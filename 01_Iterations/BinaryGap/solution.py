# https://app.codility.com/demo/results/trainingQJCVNY-T44/

def solution(N):
    # write your code in Python 3.6
    bin = "{0:b}".format(N)
    
    is_count = False
    max_count = 0
    curr_count = 0

    prev = bin[0]
    for i in range(1, len(bin)):
        curr = bin[i]
        if prev=='1' and curr=='0':
            is_count = True

        if is_count is True:
            if curr=='0':
                curr_count += 1
            else:
                is_count = False
                max_count = max(max_count, curr_count)
                curr_count = 0

    return max_count