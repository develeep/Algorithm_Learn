import sys
sys.stdin = open('input.txt', 'r')
##################################################

def pow(a,b):
    if b == 0:
        return 1
    x = pow(a,b//2)
    if b % 2 == 0:
        return x * x
    return x * x * a

T = 10
for tc in range(1, T + 1):
    t = int(input())
    a,b = map(int,input().split())
    print(f'#{t} {pow(a,b)}')