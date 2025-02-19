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

def seven(n):
    result = 0
    for i in range(len(n)):
        if int(n[-i-1]):
            result += 2 ** i
    return str(result)

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    string = input().strip()
    binary = ''
    for s in string:
        binary += change(s)
    result = []
    for i in range(7,len(binary),7):
        result.append(seven(binary[i-7:i]))
    result.append(seven(binary[i:]))
    print(f'#{tc} {" ".join(result)}')