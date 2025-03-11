import sys

sys.stdin = open("input.txt", "r")


###########################################################
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def append(parent, value):
    if not parent.left and parent.value > value:
        parent.left = Node(value)
        return
    elif not parent.right and parent.value < value:
        parent.right = Node(value)
        return
    else:
        if parent.value > value:
            append(parent.left,value)
        else:
            append(parent.right,value)

def f(parent):
    stack = []
    stack.append()
nums = []
try:
    n = int(input())
    root = Node(n)
    while 1:
        n = int(input())
        print(n)
        append(root, n)
except:
    f(root)