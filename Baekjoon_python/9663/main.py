import sys
sys.stdin = open("input.txt", "r")

###########################################################
n = int(input())
queen_y = [0]*n
queen_xy1 = [0]*(n*2)
queen_xy2 = [0]*(n*2)
# c = y축
cnt = 0
def f(c):
    global cnt
    if c == n:
        cnt += 1
        return

    # x축
    for i in range(0,n):
        if queen_y[i] or queen_xy1[c+i]or queen_xy2[c-i+n-1]:
            continue
        queen_y[i] = 1
        queen_xy1[c+i] = 1
        queen_xy2[c-i+n-1] = 1
        f(c+1)
        queen_y[i] = 0
        queen_xy1[c + i] = 0
        queen_xy2[c - i + n - 1] = 0

f(0)
print(cnt)