import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    string = input()
    stick_stack = []
    result = 0
    i = 0
    while i < len(string):
        if string[i] == '(' and string[i+1] == ')':
            result += len(stick_stack)
            i += 2
        else:
            if string[i] == '(':
                stick_stack.append('(')
            else:
                result += 1
                stick_stack.pop()
            i += 1
    print(f'#{tc} {result}')