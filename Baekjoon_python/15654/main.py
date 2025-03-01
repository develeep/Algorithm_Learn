import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
visited = [0]*n
def f(idx,arr):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            f(i+1,arr+[nums[i]])
            visited[i] = 0

f(0,[])