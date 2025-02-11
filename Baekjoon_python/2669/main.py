import sys
sys.stdin = open('input.txt', 'r')

square_arr = [list(map(int,input().split())) for _ in range(4)]
result_arr = [[[0] * 100]for _ in range(100)]
zip_arr = list(zip(*square_arr))
max_y = max(zip_arr[3])
max_x = max(zip_arr[2])
result_arr = [[0]*max_x for _ in range(max_y)]
cnt = 0
for (ax,ay,bx,by) in square_arr:
    for i in range(ay, by):
        for j in range(ax, bx):
            if result_arr[i][j]:
                continue
            result_arr[i][j] = 1
            cnt += 1
print(cnt)