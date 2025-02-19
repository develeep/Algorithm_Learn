import sys
sys.stdin = open('input.txt', 'r')
##################################################
dir = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
def change(s):
    num = s
    if s.isdigit():
        num = int(s)
    else:
        num = dir[s]
    result = [0]*4
    for i in range(4):
        result[i] = 1 if (num & (8>>i)) else 0
    return ''.join(map(str,result))

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,s = input().split()
    result = ''
    for i in range(int(n)):
        result += change(s[i])
    print(f'#{tc} {result}')
