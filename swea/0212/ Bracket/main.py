import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    string = input()
    bracket_stack = ['{']
    bracket_dir = {
        '{':'}',
        '(':')',
    }
    for s in string:
        if s in bracket_dir.keys():
            bracket_stack.append(s)
            continue
        top = bracket_stack[-1]
        if bracket_dir[top] == s:
            bracket_stack.pop()

    print(f'#{tc} {0 if len(bracket_stack)-1 else 1}')