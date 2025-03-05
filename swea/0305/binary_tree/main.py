import sys
sys.stdin = open('input.txt', 'r')
########################################
class Node:
    def __init__(self,idx):
        self.idx = idx
        self.left = 0
        self.right = 0

def first_check(idx):
    print(arr[idx].idx, end=' ')
    if arr[idx].left != 0:
        first_check(arr[idx].left)
    if arr[idx].right != 0:
        first_check(arr[idx].right)


def center_check(idx):
    if arr[idx].left != 0:
        center_check(arr[idx].left)
    print(arr[idx].idx, end=' ')
    if arr[idx].right != 0:
        center_check(arr[idx].right)

def end_check(idx):
    if arr[idx].left != 0:
        end_check(arr[idx].left)
    if arr[idx].right != 0:
        end_check(arr[idx].right)
    print(arr[idx].idx, end=' ')




v = int(input())
arr = [Node(i) for i in range(1,v+1)]
inputs = list(map(int,input().split()))
for i in range(0,len(inputs),2):
    start, end = inputs[i]-1,inputs[i+1]-1
    if arr[start].left == 0:
        arr[start].left = end
    else:
        arr[start].right = end

first_check(0)
print()
center_check(0)
print()
end_check(0)