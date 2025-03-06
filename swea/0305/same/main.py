import sys
sys.stdin = open('input.txt', 'r')
########################################
def f(idx,flag):
    global res, res_idx

    if not vertex[idx]:
        if idx == one or idx == two :
            flag += 1
        return 1, flag

    c = 1
    fl = 0
    for a in vertex[idx]:
        cnt, fla = f(a,flag)
        c += cnt
        fl += fla

    if idx == one or idx == two:
        fl += 1

    if fl == 2:
        if c < res:
            res = c
            res_idx = idx

    return c, fl


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    v,e,one,two = map(int,input().split())
    one -=1
    two -=1
    vertex = [[] for _ in range(v)]
    inputs = list(map(int,input().split()))
    for i in range(0,e*2,2):
        up, down = inputs[i],inputs[i+1]
        vertex[up-1].append(down-1)
    res = v
    res_idx = 0
    f(0,0)
    print(f'#{tc}', res_idx+1, res)