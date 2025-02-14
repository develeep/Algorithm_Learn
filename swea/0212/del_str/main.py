import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    string = input()
    result = [0]
    for i in range(len(string)):
        if result[-1] == string[i]:
            result.pop()
            continue
        result.append(string[i])
    print(f'#{tc} {len(result)-1}')
