import sys
sys.stdin = open('input.txt','r')

n = int(input())
eggs = [list(map(int,input().split())) for _ in range(n)]
# 내구도 s 무게  w 순
max_result = 0
def f(pick,cnt):
    global max_result
    max_result = max(max_result, cnt)
    if pick == n:
        return
    if eggs[pick][0] <= 0:
        f(pick+1,cnt)
        return

    for i in range(n):
        if eggs[i][0] <= 0 or i == pick:
            continue
        eggs[pick][0] -= eggs[i][1]
        eggs[i][0] -= eggs[pick][1]
        if eggs[pick][0] <= 0:
            cnt += 1
        if eggs[i][0] <= 0:
            cnt += 1
        f(pick+1,cnt)
        if eggs[pick][0] <= 0:
            cnt -= 1
        if eggs[i][0] <= 0:
            cnt -= 1
        eggs[pick][0] += eggs[i][1]
        eggs[i][0] += eggs[pick][1]

f(0,0)
print(max_result)