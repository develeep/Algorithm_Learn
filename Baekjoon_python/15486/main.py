import sys
sys.stdin = open('input.txt', 'r')
###############################################################
input = sys.readline()
n = int(input())
schedules = [list(map(int,input().split())) for _ in range(n)]
for idx, schedule in enumerate(schedules, start=1):
    schedule[0] += idx - 1

DP = [0]*(n+1)
for i in range(n):
    DP[i+1] = max(DP[i+1], DP[i])
    if schedules[i][0] <= n:
        DP[schedules[i][0]] = max(DP[schedules[i][0]], DP[i] + schedules[i][1])
print(DP[n])