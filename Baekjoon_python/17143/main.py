import sys

sys.stdin = open("input.txt", "r")

def move(arr, shark_arr, w, h):
    for i in range(len(shark_arr)):
        if not shark_arr[i]:
            continue
        r, c, s, d, z = shark_arr[i]
        arr[r-1][c-1] = 0
        if d == 1:
            if s < r:
                mh = r - s
            else:
                if ((s - (r - 1)) // (h - 1)) % 2 == 1:
                    mh = h - (s - (r - 1)) % (h - 1)
                else:
                    mh = (s - (r - 1)) % (h - 1) + 1
                    shark_arr[i][3] = 2
            shark_arr[i][0] = mh
        elif d == 2:
            if s <= (h - r):
                mh = r + s
            else:
                if ((s - (h - r)) // (h - 1)) % 2 == 0:
                    mh = h - (s - (h - r)) % (h - 1)
                    shark_arr[i][3] = 1
                else:
                    mh = (s - (h - r)) % (h - 1) + 1
            shark_arr[i][0] = mh

        elif d == 4:
            if s < c:
                mc = c - s
            else:
                if ((s - (c - 1)) // (w - 1)) % 2 == 1:
                    mc = w - (s - (c - 1)) % (w - 1)
                else:
                    mc = (s - (c - 1)) % (w - 1) + 1
                    shark_arr[i][3] = 3
            shark_arr[i][1] = mc
        elif d == 3:
            if s <= (w - c):
                mc = c + s
            else:
                if ((s - (w - c)) // (w - 1)) % 2 == 0:
                    mc = w - (s - (w - c)) % (w - 1)
                    shark_arr[i][3] = 4
                else:
                    mc = (s - (w - c)) % (w - 1) + 1
            shark_arr[i][1] = mc


    return

def update(arr,shark_arr,m):
    for i in range(m):
        if shark_arr[i] == 0:
            continue
        r = shark_arr[i][0]
        c = shark_arr[i][1]

        if arr[r - 1][c - 1]:
            shark_idx = arr[r - 1][c - 1] - 1
            if shark_arr[shark_idx][4] > shark_arr[i][4]:
                shark_arr[i] = 0
            else:
                arr[r - 1][c - 1] = i + 1
                shark_arr[shark_idx] = 0
        else:
            arr[r - 1][c - 1] = i + 1



r, c, m = map(int, input().split())
shark_arr = list(list(map(int, input().split())) for _ in range(m))
arr = [[0] * c for _ in range(r)]
count = 0
update(arr,shark_arr,m)

for i in range(c):
    for j in range(r):
        if arr[j][i]:
            shark_idx = arr[j][i] - 1
            count += shark_arr[shark_idx][4]
            arr[j][i] = 0
            shark_arr[shark_idx] = 0
            break
    move(arr, shark_arr, c, r)
    update(arr,shark_arr,m)

print(count)