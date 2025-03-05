import sys
sys.stdin = open('input.txt','r')

class stack:
    def __init__(self):
            self.top = -1
            self.arr = []

    def push(self,num):
        self.arr.append(num)
        self.top += 1

    def empty(self):
        if self.top == -1:
            return 1
        return 0

    def pop(self):
        if self.empty():
            return -1
        n = self.arr.pop()
        self.top -= 1
        return n

    def get_top(self):
        if self.empty():
            return -1
        return self.arr[self.top]

    def size(self):
        return self.top + 1

arr = stack()

n = int(input())
for _ in range(n):
    inputs = input().split()

    if inputs[0] == 'push':
        arr.push(inputs[1])
        continue

    if inputs[0] == 'top':
        print(arr.get_top())
        continue

    if inputs[0] == 'empty':
        print(arr.empty())
        continue
    if inputs[0] == 'pop':
        print(arr.pop())
        continue
    if inputs[0] == 'size':
        print(arr.size())
        continue


