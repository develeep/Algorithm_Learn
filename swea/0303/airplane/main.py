import sys
sys.stdin = open("input.txt", "r")

###########################################################
T = int(input())
for test_case in range(1,T + 1):
    n,m = map(int,input().split())
    times = [int(input()) for _ in range(n)]
    start = 1
    end = max(times) * m
    res = end
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for t in times:
            sum += mid // t
            if sum >= m:
                res = mid
                end = mid - 1
                break
        if sum < m:
            start = mid + 1
    print(f'#{test_case} {int(res)}')
