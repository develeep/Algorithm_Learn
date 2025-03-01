import sys
sys.stdin = open("input.txt", "r")

###########################################################

n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
def f(idx,arr):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(idx,n):
        f(i+1,arr+[nums[i]])

f(0,[])