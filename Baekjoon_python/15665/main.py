import sys
sys.stdin = open("input.txt", "r")

###########################################################
n,m = map(int,input().split())
nums = list(set(map(int,input().split())))
nums.sort()
arr = []
def f(c):
    global arr
    if c == m:
        print(' '.join(map(str,arr)))
        return
    for num in nums:
        arr.append(num)
        f(c+1)
        arr.pop()

f(0)