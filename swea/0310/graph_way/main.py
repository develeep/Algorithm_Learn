import sys
sys.stdin = open('input.txt', 'r')
########################################
def find_way(idx,g):
    if idx == g:
        return 1
    for i in nodes[idx]:
        if find_way(i,g):
            return 1
    return 0


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    v,e = map(int,input().split())
    nodes = [[] for _ in range(v+1)]
    for _ in range(e):
        start,end = map(int,input().split())
        nodes[start].append(end)

    s, g = map(int, input().split())
    print(f'#{tc}', find_way(s, g))
