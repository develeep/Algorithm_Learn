import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

class Node:
    def __init__(self):
        self.left = set()
        self.right = set()

    def is_left(self):
        return len(self.left) > 0

    def is_right(self):
        return len(self.right) > 0

    def pop_left(self, value):
        self.left.remove(value)


def dfs(x):
    if visited[x] == 1:
        return
    visited[x] = 1
    if nodes[x].is_left():
        for left in nodes[x].left:
            dfs(left)
    else:
        first.append(x)

    if nodes[x].is_right():
        for right in nodes[x].right:
            dfs(right)


def bfs(arr):
    history = []
    que = deque(arr)
    while que:
        x = que.popleft()
        if nodes[x].is_left() or x in history:
            continue

        history.append(x)
        for right in nodes[x].right:
            nodes[right].pop_left(x)
            que.append(right)

    return history


T = 10  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    v, e = list(map(int, input().split()))
    input_arr = list(map(int, input().split()))
    nodes = [Node() for _ in range(v + 1)]
    first = []
    visited = [0] * (v + 1)
    for i in range(e):
        start, end = input_arr[i * 2], input_arr[i * 2 + 1]
        nodes[start].right.add(end)
        nodes[end].left.add(start)

    dfs(v)

    print(f'#{tc}', ' '.join(map(str, bfs(first))))
