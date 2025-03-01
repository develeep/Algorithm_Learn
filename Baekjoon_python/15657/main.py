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

    for i in range(n):
        if i < idx:
            continue
        f(i,arr+[nums[i]])

f(0,[])