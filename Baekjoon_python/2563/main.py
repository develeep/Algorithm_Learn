import sys
sys.stdin = open("input.txt", "r")

###########################################################
s = 'A*234'

print(s.lower())
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
paper = [[0]*100 for _ in range(100)]
cnt = 0
for x,y in arr:
    for i in range(x-1,x + 9):
        for j in range(y-1, y+9):
            if paper[i][j]:
                continue
            paper[i][j] = 1
            cnt += 1

print(cnt)