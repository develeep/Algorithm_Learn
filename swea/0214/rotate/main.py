import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f'#{tc} {arr[m%n]}')
