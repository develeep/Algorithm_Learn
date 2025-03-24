import sys
sys.stdin = open('input.txt', 'r')
##################################################
v = int(input())
m = int(input())
vertex = [set() for _ in range(v+1)]
visited = [0] * (v+1)
def dfs(idx):
    visited[idx] = 1
    c = 1
    for neighbor in vertex[idx]:
        if visited[neighbor]:
            continue
        c += dfs(neighbor)
    return c

for _ in range(m):
    start, end = map(int,input().split())
    vertex[start].add(end)
    vertex[end].add(start)

print(dfs(1)-1)
