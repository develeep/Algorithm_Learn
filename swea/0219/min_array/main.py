import sys
sys.stdin = open('input.txt', 'r')
##################################################
def find_min(hap,l):
    global result
    if hap >= result:
        return
    if l == n:
        result = min(result,hap)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            find_min(hap + arr[i][l],l+1)
            visited[i] = 0

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = float('inf')
    visited = [0]*n
    find_min(0,0)
    print(f'#{tc}', result)