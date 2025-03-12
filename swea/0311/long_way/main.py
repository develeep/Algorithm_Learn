import sys

sys.stdin = open('input.txt', 'r')


########################################
def dfs(x, cnt, history):
    global res
    res = max(res, cnt)
    for node in nodes[x]:
        if node in history:
            continue
        history.add(node)
        dfs(node, cnt + 1, history)
        history.remove(node)
    return


T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    nodes = [set() for _ in range(n + 1)]
    for _ in range(m):
        start, end = map(int, input().split())
        nodes[start].add(end)
        nodes[end].add(start)
    visited = [0] * (n + 1)
    res = 0
    for i in range(1, n + 1):
        his = set()
        his.add(i)
        dfs(i, 1, his )

    print(f'#{tc}', res)
