import sys
sys.stdin = open('input.txt', 'r')
##################################################

def check(str_arr):
    index = len(str_arr) // 2
    if str_arr[:index] == str_arr[-1:-index-1:-1]:
        return 1
    return 0

T = 10    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    k = int(input())

    arr = [[*input()] for _ in range(8)]
    zip_arr = list(zip(*arr))
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)-k+1):
            cnt += check(arr[i][j:j + k])
            cnt += check(zip_arr[i][j:j + k])
    print(f'#{tc} {cnt}')

