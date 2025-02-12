import sys
sys.stdin = open('input.txt', 'r')
##################################################





def check(ax,ay,bx,by):
    if ax[0] > bx[1] or ax[1] < bx[0] or ay[0] > by[1] or ay[1] < by[0]:
        return 'd'
    if ax[0] == bx[0] and ax[1] == bx[1] and ay[0] == by[0] and ay[1] == by[1]:
        return 'a'
    for i in range(4):
        if ax[i % 2] == bx[1 - i % 2] and ay[i // 2] == by[int(i // 2 == 0)]:
            return 'c'
    for i in range(2):
        if ax[i] == bx[i == 0] or ay[i] == by[i == 0]:
            return 'b'
    return 'a'

for _ in range(4):
    arr = list(map(int, input().split()))
    ax = [arr[0], arr[2]]
    ay = [arr[1], arr[3]]
    bx = [arr[4], arr[6]]
    by = [arr[5], arr[7]]
    print(check(ax,ay,bx,by))