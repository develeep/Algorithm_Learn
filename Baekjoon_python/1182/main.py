import sys
sys.stdin = open('input.txt','r')

n,s = map(int,input().split())
nums = list(map(int,input().split()))
result = 0
def f(idx,cnt):
    global result
    if idx == n:
        if cnt == s:
            result += 1
        return

    f(idx+1, cnt+nums[idx])

    f(idx+1, cnt)

f(0,0)
print(result-1 if s == 0 else result)