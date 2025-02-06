import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))

    for idx in range(10):
        next_arr = arr[idx:]
        if idx % 2 == 0:
            max_idx = next_arr.index(max(next_arr)) + idx
            arr[max_idx], arr[idx] = arr[idx], arr[max_idx]
        else:
            min_idx = next_arr.index(min(next_arr)) + idx
            arr[min_idx], arr[idx] = arr[idx], arr[min_idx]

    print(f'#{tc}', *arr)