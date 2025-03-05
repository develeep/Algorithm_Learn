import sys
sys.stdin = open('input.txt', 'r')
########################################
class Node:
    def __init__(self):
        self.value = None
        self.left = 0
        self.right = 0


def cal(idx):
    if arr[idx].value.isnumeric():
        return int(arr[idx].value)

    a,b = cal(arr[idx].left), cal(arr[idx].right)

    if arr[idx].value == '+':
        return a+b
    elif arr[idx].value == '-':
        return a-b
    elif arr[idx].value == '*':
        return a*b
    elif arr[idx].value == '/':
        return a/b

T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [Node() for _ in range(n)]

    for i in range(n):
        inputs = input().split()
        arr[i].value = inputs[1]
        if inputs[1].isnumeric():
            continue
        arr[i].left = int(inputs[2])-1
        arr[i].right = int(inputs[3])-1

    print(f'#{tc}', int(cal(0)))