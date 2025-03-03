import sys
sys.stdin = open("input.txt", "r")

###########################################################
papers = [list(map(int,input().split())) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
def f(x,y,i,n):
    nx,ny = x + (i//n), y + (i%n)

    if not (0<=nx<10 and 0<=ny<10):
        return 0
    if papers[nx][ny] == 0:
        return 0
    if visited[nx][ny]:
        return 0

    if i == n:
        return 1

    visited[nx][ny] = f(nx,ny,i+1,n)
    return visited[nx][ny]

def dfs(x,y):

    for i in range(10):
        for j in range(10):
            if visited[i][j] == 0:
                for d in range(1,6):
                    f(i,j,0,25)
