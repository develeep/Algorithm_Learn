import sys
sys.stdin = open('input.txt', 'r')
##################################################
# def get_word(start,end,string):
#     word = ''
#     for i in range(start,end,-1):
#         if string[i].isdigit():
#             word = string[i] + word
#         if string[i-1] == ' ':
#             break
#     return word, i-2
#
#
# T = int(input())    # Testcase 개수를 받아오는 코드
# for tc in range(1, T + 1):
#     n = int(input())
#     string = input()
#     result = 0
#     max_result = 0
#     i = len(string)-1
#     while i >= 0:
#         num, idx = get_word(i,-1,string)
#         num = int(num)
#         i = idx
#         if max_result < num:
#             max_result = num
#         elif num == max_result:
#             continue
#         else:
#             result += max_result - num

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    string = input()
    p = 1
    max_result = 0
    result = 0
    num = 0

    for s in string[::-1]:
        if s == ' ':
            if max_result < num:
                max_result = num
            elif max_result > num:
                result += max_result - num
            num = 0
            p = 1
        else:
            num += int(s) * p
            p *= 10
    if max_result > num:
        result += max_result - num
    print(f'#{tc} {result}')
