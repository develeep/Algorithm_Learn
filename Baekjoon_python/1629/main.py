import sys
sys.stdin = open('input.txt', 'r')
########################################
a,b,c = map(int,input().split())
def f(a,b):
    if b == 1:
        return a%c
    res = f(a,b//2)%c

    if b%2 == 0:
        return (res*res)%c
    else:
        return (res*res*a)%c

print(f(a,b))