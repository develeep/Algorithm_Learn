import sys
sys.stdin = open("input.txt", "r")

###########################################################


def main():
    n,m = map(int,input().split())
    nodes = [[] for _ in range(n+1)]
    visited = [0]*(n+1)

    for _ in range(m):
        s,e = map(int,input().split())
        nodes[s].append(e)
        nodes[e].append(s)
    cnt = 0
    def dfs(n):
        stack = [n]
        while stack:
            for node in nodes[stack.pop()]:
                if visited[node] == 0:
                    visited[node] = 1
                    stack.append(node)


    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            cnt += 1

    print(cnt)

main()