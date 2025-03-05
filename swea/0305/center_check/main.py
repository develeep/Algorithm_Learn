import sys
sys.stdin = open('input.txt', 'r')
########################################
class Node():
    def __init__(self,value,left,right):
        self.value = value
        self.left = left
        self.right = right

def find(idx):
        if arr[idx].left != 0:
            find(arr[idx].left)
        print(arr[idx].value, end='')
        if arr[idx].right != 0:
            find(arr[idx].right)



T = 10     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    arr = [None]
    for _ in range(n):
        inputs = input().split()
        node = Node(inputs[1],int(inputs[2]) if len(inputs) > 2 else 0,int(inputs[3]) if len(inputs) > 3 else 0)
        arr.append(node)
    print(f'#{tc}',end=' ')
    find(1)
    print()