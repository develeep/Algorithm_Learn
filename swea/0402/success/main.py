import sys
sys.stdin = open('input.txt', 'r')
###############################################################

T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    grid = tuple(tuple(map(int,input().split())) for _ in range(n))
    res = 0
    print(res)