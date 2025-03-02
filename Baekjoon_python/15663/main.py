import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
used = [0]*n
def f(arr):
    t = 0
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return

    for i in range(len(nums)):
        if used[i] == 0 and t != nums[i]:
            used[i] = 1
            t = nums[i]
            f(arr+[nums[i]])
            used[i] = 0
f([])