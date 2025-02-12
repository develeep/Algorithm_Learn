import sys
sys.stdin = open('input.txt', 'r')
##################################################

bingo = [x for _ in range(5) for x in map(int,input().split())]
answer_arr = [x for i in range(5) for x in map(int,input().split())]

for answer_index in range(len(answer_arr)):
    answer = answer_arr[answer_index]
    index = bingo.index(answer)
    bingo[index] = 0
    if answer_index < 10:
        continue

    btm_up = 0
    up_btm = 0
    cnt = 0
    for i in range(5):
        x_hap = 0
        y_hap = 0
        for j in range(5):
            x_hap += bingo[i*5+j]
            y_hap += bingo[j*5+i]
        btm_up += bingo[(i+1)*5 - i - 1]
        up_btm += bingo[i*5+i]
        if not x_hap > 0:
            cnt += 1
        if not y_hap > 0:
            cnt += 1
    cnt_up = 0 if up_btm > 0 else 1
    cnt_btm = 0 if btm_up > 0 else 1
    if cnt + cnt_up + cnt_btm >= 3:
        print(answer_index+1)
        break
