import sys
sys.stdin = open('input.txt', 'r')
########################################
import itertools
def dfs(i,j,first_cost):
    res = 0
    for r in range(i,n):
        for idx in range(j if r == i else 0,n-m+1):
            second_bee = honeys[r][idx:idx+m]
            res = max(res,first_cost + get(second_bee))
    return res


def get(bees):
    result = 0
    for i in range(1,m+1):
        for comb in itertools.combinations(bees,i):
            if sum(comb) > c:
                continue
            cost = sum([com**2 for com in comb])
            result = max(result,cost)
    return result

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,m,c = map(int,input().split())
    honeys = [list(map(int,input().split())) for _ in range(n)]
    res = 0

    for i in range(n):
        for j in range(n-m+1):
            first_bee = honeys[i][j:j+m]
            res = max(res,dfs(i,j+m,get(first_bee)))
    print(f'#{tc}', res)
