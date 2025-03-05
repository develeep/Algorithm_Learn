import sys
sys.stdin = open('input.txt', 'r')
########################################
class Node:
    def __init__(self):
        self.value = 0
        self.left = 0
        self.right = 0

    def append(self,idx,c):
        if c == 0:
            self.left = idx
        else:
            self.right = idx

def cal(idx):
    if idx == 0:
        return 0
    if arr[idx].value != 0:
        return arr[idx].value
    arr[idx].value = cal(arr[idx].left) + cal(arr[idx].right)
    return arr[idx].value

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n, m, choice = map(int, input().strip().split())
    arr = [0]
    for i in range(1,n+1):
        node = Node()
        if i > 1:
            arr[i//2].append(i,i%2)
        arr.append(node)

    for _ in range(m):
        idx, num = map(int,input().split())
        arr[idx].value = num

    cal(choice)
    print(f'#{tc}', arr[choice].value)