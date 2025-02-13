import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = 10   # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    s = input()
    stack = []
    cal = []
    result = 0
    for i in range(n):
        if s[i] == '+':
            cal.append(cal)
            continue
        stack.append(int(s[i]))
        if len(cal) > 0:
            stack.append(stack.pop() + stack.pop())
            cal.pop()
    print(f'#{tc} {stack[0]}')