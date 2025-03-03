import sys

sys.stdin = open("input.txt", "r")

###########################################################
from collections import deque


def check(arr):
    q = deque([arr[0]])
    visited = [0] * n
    visited[arr[0]] = 1
    cnt = 1
    cost = users[arr[0]]
    while q:
        idx = q.popleft()
        for next_idx in nodes[idx]:
            next_idx -= 1
            if visited[next_idx]:
                continue
            if next_idx in arr:
                visited[next_idx] = 1
                q.append(next_idx)
                cnt += 1
                cost += users[next_idx]

    if len(arr) != cnt:
        return -1

    return cost


def f(depth):
    global result
    if depth == n:
        if not (red and blue):
            return
        cost_red = check(red)
        cost_blue = check(blue)
        if cost_red == -1 or cost_blue == -1:
            return
        result = min(result, abs(cost_red - cost_blue))
        return

    red.append(depth)
    f(depth + 1)
    red.pop()
    blue.append(depth)
    f(depth + 1)
    blue.pop()


n = int(input())
users = list(map(int, input().split()))
nodes = []
result = float('inf')

for _ in range(n):
    m, *neighbor = map(int, input().split())
    nodes.append(neighbor)
red = []
blue = []
f(0)
print(-1 if result == float('inf') else result )
