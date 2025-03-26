import sys
sys.stdin = open('input.txt', 'r')
########################################
def f():
    if n == 2:
        return stairs[1]+stairs[0]
    if n == 1:
        return stairs[0]
    DP = [0,stairs[0], stairs[1]+stairs[0]]

    for i in range(3, n+1):
        DP.append(max((stairs[i-1] + stairs[i-2] + DP[i-3]), (stairs[i-1] + DP[i-2])))
    return DP[n]

n = int(input())
stairs = [int(input()) for _ in range(n)]
print(f())