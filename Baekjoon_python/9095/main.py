import sys
sys.stdin = open('input.txt', 'r')
########################################
t = int(input())
DP = [0] * 11
DP[1] = 1
DP[2] = 2
DP[3] = 4
for i in range(4, 11):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

for _ in range(t):
    print(DP[int(input())])