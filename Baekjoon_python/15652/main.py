import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,m = map(int,input().split())
def f(arr):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1,n+1):
        if arr and arr[-1] > i:
            continue
        f(arr+[i])

f([])