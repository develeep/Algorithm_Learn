import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    result = ''
    i = 0
    j = 0
    for s,cnt in arr:
        result += s*int(cnt)
    print(f'#{tc}')
    for i in range(0,len(result),10):
        print(result[i:i+10])
