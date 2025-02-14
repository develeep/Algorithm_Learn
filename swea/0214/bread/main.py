import sys
sys.stdin = open('input.txt', 'r')
##################################################
T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,m,k = map(int,input().split())
    user_arr = sorted(map(int,input().split()))
    result = 1
    for i in range(len(user_arr)):
        if i >= (user_arr[i] // m) * k:
            result = 0
            break
    print(f'#{tc} {"Possible" if result else "Impossible"}')
