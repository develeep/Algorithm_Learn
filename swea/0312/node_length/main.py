import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
def bfs(start):
    q = deque()
    q.append((start, 1))
    visited = [0]*(v+1)
    while q:
        node, depth = q.popleft()
        for neighbor in nodes[node]:
            if visited[neighbor]:
                continue
            if neighbor == end:
                return depth
            visited[neighbor] = 1
            q.append((neighbor, depth+1))
    return 0

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    v,e = map(int,input().split())
    nodes = [[] for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int,input().split())
        nodes[start].append(end)
        nodes[end].append(start)
    start, end = map(int,input().split())
    print(f'#{tc}', bfs(start))
