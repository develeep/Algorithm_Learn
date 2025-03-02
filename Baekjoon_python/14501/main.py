import sys
sys.stdin = open("input.txt", "r")

###########################################################
n = int(input())
schedules = [list(map(int,input().split())) for _ in range(n)]
max_result = 0
def f(t,total):
    global max_result
    max_result = max(max_result, total)
    for idx in range(t,n):
        if idx + schedules[idx][0] <= n:
            f(idx+schedules[idx][0], total+schedules[idx][1])

f(0,0)
print(max_result)