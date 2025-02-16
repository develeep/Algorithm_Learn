import sys
sys.stdin = open("input.txt", "r")

###########################################################

T = int(input())
for test_case in range(1,T + 1):
    n,m = map(int,input().split())
    arr = [input() for _ in range(n)]
    min_change = n*m
    for i in range(1,n-1):
        for j in range(i+1,n):
            w = ''.join(arr[:i])
            b = ''.join(arr[i:j])
            r = ''.join(arr[j:])
            change_white = i - w.count('W')
            change_blue = j-i - b.count('B')
            change_red = n*m-j - r.count('R')
            change_color = sum([change_blue, change_white, change_red])
            min_change = min(min_change, change_color)
    print(f'#{test_case} {min_change}')