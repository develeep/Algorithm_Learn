import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0]*10 for _ in range(10)]
    color_arr = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for color in color_arr:
        x1,y1,x2,y2,c = color
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if not arr[i][j]:
                    arr[i][j] = c
                else:
                    if arr[i][j] != c and arr[i][j] != 3:
                        arr[i][j] = 3
                        cnt += 1
    print(f'#{tc} {cnt}')