import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
def f(arr):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        f(arr+[nums[i]])

f([])