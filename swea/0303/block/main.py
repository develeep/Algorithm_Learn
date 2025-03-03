import sys

sys.stdin = open("input.txt", "r")

###########################################################
from collections import deque
from copy import deepcopy

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))


def pangs(q, block_arr):
    x, y, depth = q.popleft()
    block_arr[x][y] = 0
    c = 1
    for i in range(1, depth):
        for dx, dy in dxy:
            nx, ny = x + dx * i, y + dy * i
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if block_arr[nx][ny] == 0:
                continue
            if block_arr[nx][ny] > 1:
                q.append((nx, ny, block_arr[nx][ny]))
            else:
                c += 1
            block_arr[nx][ny] = 0
    return c


def find_block(pick,block_arr):
    for idx in range(h):
        if block_arr[idx][pick]:
            return idx
    return -1


def block_down(block_arr):
    for i in range(w):
        while 1:
            flag = 0
            for j in range(h - 1):
                if block_arr[j][i] and block_arr[j + 1][i] == 0:
                    flag = 1
                    block_arr[j][i], block_arr[j + 1][i] = block_arr[j + 1][i], block_arr[j][i]
            if flag == 0:
                break


def pang(picks,block_arr):
    cnt = 0
    for p in picks:
        x = find_block(p,block_arr)
        if x == -1:
            return cnt
        q = deque([(x, p, block_arr[x][p])])
        while q:
            cnt += pangs(q,block_arr)
        block_down(block_arr)
    return cnt


def f(picks):
    global result
    if result == h*w:
        return
    if len(picks) == n:
        block_arr = deepcopy(blocks)
        cnt = pang(picks, block_arr)
        result = max(result, cnt)
        return
    for i in range(w):
        f(picks + [i])

T = int(input())
for test_case in range(1, T + 1):
    n, w, h = map(int, input().strip().split())
    blocks = [list(map(int, input().split())) for _ in range(h)]
    max_block = 0
    for i in range(h):
        for j in range(w):
            max_block += blocks[i][j] > 0
    result = 0
    f([])

    print(f'#{test_case}',max_block - result)
