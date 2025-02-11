import sys

sys.stdin = open('input.txt', 'r')


##################################################

def ladder(x, y, arr):
    dx = [1, 0, 0]
    dy = [0, -1, 1]
    history = [0,0]
    cnt = 0
    while x < 99:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 100 and 0 <= ny < 100 and [nx, ny] != history and arr[nx][ny]:
                history = [x, y]
                x, y = nx, ny
                cnt += 1
    return cnt


T = 10  # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    t = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    min_result = 1000
    result = 0
    for i in range(100):
        if arr[0][i]:
            cnt = ladder(0, i, arr)
            if cnt < min_result:
                result = i
                min_result = cnt

    print(f'#{t} {result}')
