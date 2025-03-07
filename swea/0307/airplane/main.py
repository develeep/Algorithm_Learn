import sys
sys.stdin = open('input.txt', 'r')
########################################
def check(arr):
    his = [0]*n
    for i in range(1,n):
        if abs(arr[i-1] - arr[i]) > 1:
            return 0
        if arr[i-1] == arr[i]:
            continue

        if arr[i-1] > arr[i]:
            if i + x > n:
                return 0
            for j in range(x):
                if his[i+j]:
                    return 0
                his[i+j] = arr[i]
            continue

        if arr[i-1] < arr[i]:
            if i < x:
                return 0
            for j in range(1,x+1):
                if his[i - j]:
                    return 0
                his[i - j] = arr[i]
    return 1
T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,x = map(int,input().split())
    air_arr= [list(map(int,input().split())) for i in range(n)]
    zip_arr = list(zip(*air_arr))
    res = 0
    for idx in range(n):
        if check(air_arr[idx]):
            res += 1
        if check(zip_arr[idx]):
            res += 1

    print(f'#{tc}',res)