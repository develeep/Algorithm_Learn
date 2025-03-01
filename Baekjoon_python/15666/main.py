import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,m = map(int,input().split())
nums = list(set(map(int,input().split())))
nums.sort()

def f(arr):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return

    for num in nums:
        if arr and arr[-1] > num:
            continue

        f(arr+[num])

f([])