import sys
sys.stdin = open('input.txt', 'r')
##################################################

def isValid(arr):
    result = []
    for i in range(len(arr)):
        if len(arr) % 2 == 1 and i == len(arr)//2:
            continue
        if i < len(arr) // 2:
            result.append(arr[i])
            continue

        if result.pop() == arr[i]:
            continue
        else:
            return False
    return len(result) == 0


T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    result = ''
    arr = [[*input()] for _ in range(n)]
    zip_arr = list(zip(*arr))
    for i in range(n):
        if result:
            break
        for j in range(n-m+1):
            r_arr = arr[i][j:j+m]
            c_arr = zip_arr[i][j:j+m]
            if isValid(r_arr):
                result = ''.join(r_arr)
                break
            if isValid(c_arr):
                result = ''.join(c_arr)
                break
    print(f'#{tc} {result}')
