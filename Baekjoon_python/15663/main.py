import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visited = {}
used = [0]*n
def f(arr):
    if len(arr) == m:
        if tuple(arr) in visited:
            return
        visited[tuple(arr)] = 1
        print(*arr)
        return

    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            f(arr+[nums[i]])
            used[i] = 0
f([])