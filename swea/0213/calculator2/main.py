import sys
sys.stdin = open('input.txt', 'r')
##################################################

dic = {'+':0,'*':1}

def parse(string):
    cal = []
    stack = []
    for s in string:
        if s.isdigit():
            stack.append(s)
        else:
            if len(cal) and dic[cal[-1]] >= dic[s]:
                c = cal.pop()
                stack.append(c)
            cal.append(s)
    while cal:
        stack.append(cal.pop())
    return stack

def cal(string):
    stack = []
    for s in string:
        if s.isdigit():
            stack.append(int(s))
        else:
            a = stack.pop()
            b = stack.pop()
            if dic[s]:
                stack.append(a*b)
            else:
                stack.append(a+b)
    return stack[0]


T = 10
for tc in range(1, T + 1):
    s = input()
    string = input()
    p = parse(string)
    s = cal(p)
    print(f'#{tc} {s}')