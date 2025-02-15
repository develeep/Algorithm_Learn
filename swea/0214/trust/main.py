import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, *arr = list(input().split())
    b = []
    o = []
    color_arr = deque()
    t = 0
    for i in range(0,len(arr) - 1,2):
        color = arr[i]
        color_arr.append(color)
        if color == 'B':
            if b:
                x = int(arr[i+1])
                move = abs(x - b[-1][1]) + 1
            else:
                move = x = int(arr[i+1])
            b.append([move,x])
        else:
            if o:
                x = int(arr[i + 1])
                move = abs(x - o[-1][1]) + 1
            else:
                move = x = int(arr[i + 1])
            o.append([move, x])
    b = deque(list(zip(*b))[0]) if b else ()
    o = deque(list(zip(*o))[0]) if o else ()
    b_move = b.popleft() if b else 101
    o_move = o.popleft() if o else 101
    while 1:
        if not color_arr:
            break
        c = color_arr.popleft()
        if c == 'B':
            if b_move > 0:
                t += b_move
                o_move -= b_move
            else:
                t += 1
                o_move -= 1
            b_move = b.popleft() if b else 101
        else:
            if o_move > 0:
                t += o_move
                b_move -= o_move
            else:
                t += 1
                b_move -= 1
            o_move = o.popleft() if o else 101

    print(f'#{tc} {t}')