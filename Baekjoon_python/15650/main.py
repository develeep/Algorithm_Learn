import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
def f(i,arr):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(i,n):
        f(i+1,arr+[i+1])

f(0,[])