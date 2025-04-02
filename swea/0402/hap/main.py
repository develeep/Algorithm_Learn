import sys
sys.stdin = open('input.txt', 'r')
###############################################################
def find_p(idx):
    if idx != nodes[idx]:
        nodes[idx] = find_p(nodes[idx])
    return nodes[idx]

T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,m = map(int,input().split())
    nodes = list(range(n+1))
    res = []
    for _ in range(m):
        s,a,b = map(int,input().split())
        pa, pb = find_p(a), find_p(b)
        if s == 0:
            if pa > pb:
                nodes[pa] = nodes[pb]
            else:
                nodes[pb] = nodes[pa]
        if s == 1:
            if pa == pb:
                res.append('1')
            else:
                res.append('0')

    print(f'#{tc}', ''.join(res))