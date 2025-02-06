import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = 10   # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    line = 0
    row = 0
    up_btm = 0
    btm_up = 0
    for i in range(100):
        li = sum(arr[i])
        r = sum([arr[j][i] for j in range(100)])
        up_btm += arr[i][i]
        btm_up += arr[99-i][i]
        if li > line:
            line = li
        if r > row:
            row = r

    result = max(line, row, up_btm, btm_up)
    print(f'#{t} {result}')
