import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input().strip())
    time_arr = [tuple(map(int,input().split())) for _ in range(n)]
    time_arr.sort(key = lambda x:x[1])
    t = 0
    result = 0
    for s,e in time_arr:
        if t > s:
            continue
        result += 1
        t = e
    print(f'#{tc} {result}')