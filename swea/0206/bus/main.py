import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    k, n, m = map(int,input().split())
    move_arr = list(map(int,input().split()))
    count = 0
    i = 1

    arr = [0] * n
    for move in move_arr:
        arr[move] = 1

    while i < n:
        if i + k <= n:
            for idx in range(k-1, -1, -1):
                if arr[i+idx] == 1:
                    count += 1
                    i += idx
                    break
            else:
                count = 0
                break
        i += 1

    print(f'#{tc} {count}')
