import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,k = map(int,input().split())

items = [list(map(int,input().split())) for _ in range(n)]

DP = [[0]*(k+1) for _ in range(n)]

for i in range(n):
    for j in range(1,k+1):
        if i == 0:
            if items[i][0] <= j:
                DP[i][j] = items[i][1]
            continue
        if j < items[i][0]:
            DP[i][j] = DP[i-1][j]
            continue
        DP[i][j] = max(DP[i-1][j], DP[i-1][j-items[i][0]] + items[i][1])

print(DP[n-1][k])