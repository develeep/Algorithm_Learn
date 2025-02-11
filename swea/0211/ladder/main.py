import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = 1    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    # dx = [0,-1,0]
    # dy = [-1,0,1]
    # direction = 1
    # flag = False
    start = arr[-1].index(2)
    # position = [99,start]
    #
    # while 1:
    #     if position[0] == 0:
    #         break
    #     if flag and arr[position[0]-1][position[1]] == 1:
    #         flag = False
    #         direction = 1
    #     elif not flag and position[1] - 1 >= 0 and arr[position[0]][position[1]-1] == 1:
    #         flag = True
    #         direction = 0
    #     elif not flag and position[1] + 1 < 100 and arr[position[0]][position[1]+1] == 1:
    #         flag = True
    #         direction = 2
    #
    #     position[0] += dx[direction]
    #     position[1] += dy[direction]

    # print(f'#{t} {position[1]}')
    dx = [-1,0,0]
    dy = [0,-1,1]

    x,y = 99,start

    while x != 0:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny]:
                arr[x][y] = 0
                x,y = nx, ny
