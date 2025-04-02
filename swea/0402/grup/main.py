import sys
sys.stdin = open('input.txt', 'r')
###############################################################
def find_p(idx):
    if nodes[idx] == idx:
        return idx
    return find_p(nodes[idx])

T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,m = map(int,input().split())
    nums = tuple(map(int,input().split()))
    nodes = list(range(n+1))

    for i in range(0, len(nums), 2):
        start, end = nums[i], nums[i+1]
        ps = find_p(start)
        pe = find_p(end)
        if ps == pe:
            continue
        nodes[pe] = ps

    cnt = 0
    for idx,node in enumerate(nodes):
        if idx == 0:
            continue
        if idx == node:
            cnt += 1
    print(f'#{tc}', cnt)