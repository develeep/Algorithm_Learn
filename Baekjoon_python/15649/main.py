import sys
sys.stdin = open("input.txt", "r")

###########################################################
def f(idx,arr):
    if len(arr) == m:
        print(*arr)
        return

    f(idx+1, arr+[idx])

    f(idx+1, arr)

n,m = map(int,input().split())
visited = [0]*(n+1)
f(1,[])