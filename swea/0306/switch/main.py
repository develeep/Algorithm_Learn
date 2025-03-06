import sys
sys.stdin = open('input.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if Ai[i] != Bi[i]:
            cnt += 1
            for j in range(i,n):
                Ai[j] = 0 if Ai[j] else 1

    print(f'#{tc}',cnt)

