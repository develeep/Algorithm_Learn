import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
cache = []
visited = [0]*n
def f(idx, arr):
    if len(arr) == m:
        if arr in cache:
            return
        cache.append(arr)
        print(*arr)
        return
    for i in range(idx,n):
        if visited[i] or nums[idx] > nums[i]:
            continue
        visited[i] = 1
        f(i+1,arr+[nums[i]])
        visited[i] = 0

f(0,[])