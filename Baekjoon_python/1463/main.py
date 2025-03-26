import sys
sys.stdin = open('input.txt', 'r')
########################################
n = int(input())
DP = [0] * (n+1)

for i in range(2,n+1):
    DP[i] = min(DP[i-1] + 1,DP[i//2] + 1 if i % 2 == 0 else 100000000000, DP[i//3] +1  if i%3 == 0 else 1000000000)

print(DP[n])