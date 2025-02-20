import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input().strip())
    arr = [2,3,5,7,11]
    print(f'#{tc}', end=" ")
    for a in arr:
        cnt = 0
        new_n = n
        while 1:
            if new_n % a:
                break
            new_n /= a
            cnt += 1
        print(cnt,end=' ')

    print()