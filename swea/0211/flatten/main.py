import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = 10    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input().split()))

    for _ in range(n):
        max_box = max(arr)
        min_box = min(arr)
        max_idx = arr.index(max_box)
        min_idx = arr.index(min_box)

        if max_box - min_box <= 1:
            result = max_box - min_box
            break

        arr[max_idx] -= 1
        arr[min_idx] += 1
    else:
        result = max(arr) - min(arr)

    print(f'#{tc} {result}')