import sys
sys.stdin = open('input.txt', 'r')
##################################################

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    string = input()
    s = ['.#..' ,'#.#.','.%s.#','#.#.','.#..']
    result = ['' for _ in range(5)]
    for i in range(len(string)):
        for j in range(5):
            if i == 0:
                if j == 2:
                    replaced_str = s[j].replace('%s', string[i])
                    result[j] += '#' + replaced_str
                else:
                    result[j] += '.' + s[j]
            else:
                if j == 2:
                    replaced_str = s[j].replace('%s', string[i])
                    result[j] += replaced_str
                else:
                    result[j] += s[j]
    print(*result, sep="\n")
