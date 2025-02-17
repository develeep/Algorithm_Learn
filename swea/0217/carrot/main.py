import sys
sys.stdin = open('input.txt', 'r')
##################################################
T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    carrot_arr = list(map(int,input().split()))
    result = 1
    hap = 1
    for i in range(n-1):
        if carrot_arr[i] < carrot_arr[i+1]:
            hap += 1
        else:
            result = max(result, hap)
            hap = 1
    result = max(result,hap)
    print(f'#{tc} {result}')
