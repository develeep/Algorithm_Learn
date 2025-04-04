import sys
sys.stdin = open('input.txt', 'r')
###############################################################
T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    grid = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if i == j :
                grid[i].append(1)
            elif j == 0:
                grid[i].append(1)
            else:
                grid[i].append(grid[i-1][j] + grid[i-1][j-1])

    print(f'#{tc}')
    print('\n'.join(map(lambda x: ' '.join(map(str,x)), grid)))