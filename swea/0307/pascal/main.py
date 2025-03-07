import sys
sys.stdin = open('input.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if i < 2 or j == 0 or j == i:
                arr[i].append(1)
            else:
                arr[i].append(arr[i-1][j-1] + arr[i-1][j])

    print(f'#{tc}')
    print('\n'.join(map(lambda x: ' '.join(map(str,x)), arr)))
