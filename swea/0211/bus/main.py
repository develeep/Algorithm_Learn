import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    bus = [list(map(int,input().split())) for _ in range(n)]
    p = int(input())
    bus_stop = [int(input()) for _ in range(p)]
    result = []

    for stop in bus_stop:
        cnt = 0
        for a,b in bus:
            if a <= stop <= b:
                cnt += 1
        result.append(str(cnt))
    print(f'#{tc} {" ".join(result)}')
