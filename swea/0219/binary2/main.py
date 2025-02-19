import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = float(input().strip())
    cnt = 1
    result = ''
    while cnt < 13 and n != 0:
        result += str(int(n//(2 ** -cnt)))
        n = n % (2 ** -cnt)
        cnt += 1
    print(f'#{tc}', result if not n else 'overflow')