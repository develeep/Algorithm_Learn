import sys
sys.stdin = open("input.txt", "r")

###########################################################
from collections import deque
def dfs(start):
    res = [start]
    for neibor in nodes[start]:
        if visited[neibor] == 1:
            continue
        visited[neibor] = 1
        res.extend(dfs(neibor))
    return res

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0]*(n+1)
    visited[start] = 1
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for neibor in nodes[node]:
            if visited[neibor]:
                continue
            visited[neibor] = 1
            q.append(neibor)
    return res


n,m,v = map(int,input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int,input().split())
    nodes[s].append(e)
    nodes[e].append(s)
for node in nodes:
    node.sort()
visited = [0]*(n+1)
visited[v] = 1
print(*dfs(v))
print(*bfs(v))