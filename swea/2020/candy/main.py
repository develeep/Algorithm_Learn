import sys
sys.stdin = open('input.txt', 'r')
##################################################
T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    min_result = float('inf')
    if n == k:
        print(f'#{tc} {arr[-1] - arr[0]}')
    else:
        for i in range(n-k+1):
            min_result = min(min_result, arr[i+k-1] - arr[i])
        print(f'#{tc} {min_result}')
