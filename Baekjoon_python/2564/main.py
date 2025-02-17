import sys
sys.stdin = open('input.txt', 'r')
##################################################
dir = [2,1,4,3]
w,h = map(int,input().split())
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
x = list(map(int,input().split()))
result = 0
for shop in arr:
    if x[0] == shop[0]:
        result += abs(x[1]-shop[1])
    elif x[0] == dir[shop[0]-1]:
        if x[0] == 1 or x[0] == 2:
            a = h + x[1] + shop[1]
            b = h + w - x[1] + w - shop[1]
            result += min(a,b)
        else:
            a = w + x[1] + shop[1]
            b = w + h - x[1] + h - shop[1]
            result += min(a,b)
    else:
        if x[0] == 1:
            if shop[0] == 3:
                result += x[1] + shop[1]
            else:
                result += w - x[1] + shop[1]
        if x[0] == 2:
            if shop[0] == 3:
                result += x[1] + h - shop[1]
            else:
                result += w - x[1] + h - shop[1]
        if x[0] == 3:
            if shop[0] == 1:
                result += x[1] + shop[1]
            else :
                result += h-x[1] + shop[1]
        if x[0] == 4:
            if shop[0] == 1:
                result += x[1] + w - shop[1]
            else :
                result += h-x[1] + w - shop[1]

print(result)