import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import  deque
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0]*101
    visited[start] = 1
    res = [0, start]
    while q:
        node, depth = q.popleft()
        neighbors = nodes.setdefault(node, 0)
        if not neighbors:
            continue
        for neighbor in neighbors:
            if visited[neighbor]:
                continue
            if res[0] < depth + 1:
                res = [depth+1, neighbor]
            if (res[0] == depth + 1) and res[1] < neighbor:
                res[1] = neighbor
            visited[neighbor] = 1
            q.append((neighbor, depth+1))
    return res[1]


T = 10    # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n, s = map(int,input().split())
    nodes = {}
    inputs = list(map(int,input().split()))
    for i in range(0, len(inputs), 2):
        start, end = inputs[i], inputs[i+1]
        if start in nodes:
            nodes[start].add(end)
        else:
            nodes[start] = set([end])
    print(f'#{tc}', bfs(s))