import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(n)]
    result = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            hap = 0
            for cnt in range(m):
                hap += sum(arr[i+cnt][j:j+m])
            result = max(result, hap)

    print(f'#{tc} {result}')