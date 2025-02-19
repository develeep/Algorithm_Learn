import sys
sys.stdin = open('input.txt', 'r')
##################################################

def change(b):
    result = 0
    for i in range(7):
        if int(b[-i - 1]):
            result += 2 ** i
    return str(result)

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input().strip())
    binary = ''.join([input().strip() for _ in range(n)])
    result = []
    for i in range(len(binary)//7):
        result.append(change(binary[7*i:7*i+7]))
    print(f'#{tc}',' '.join(result))