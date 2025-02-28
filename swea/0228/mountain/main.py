import sys
sys.stdin = open('input.txt', 'r')
##################################################
import heapq
dxy = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y,special,depth):
    if special==0:
        return

    possible_points = []
    for dx,dy in dxy:
        nx,ny = x+dx, y+dy
        if not(0<=nx<n and 0<=ny<n):
            continue
        if arr[nx][ny] < arr[x][y]:
            possible_points.append((arr[nx][ny],nx,ny,0))
            continue


T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,k = map(int,input().split())
    arr = [tuple(map(int,input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    cache = {}
    max_h = 0
    for i in range(n):
        for j in range(n):
            max_h = max(max_h, arr[i][j])

    high_mountain = [(i,j) for i in range(n) for j in range(n) if arr[i][j] == max_h]

    for hx,hy in high_mountain:
        visited[(hx,hy)] = 1
        dfs(hx,hy)
