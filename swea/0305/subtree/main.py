import sys
sys.stdin = open('input.txt', 'r')
########################################
class Node:
    def __init__(self):
        self.down = []

def f(idx):
    if not arr[idx].down:
        return 1

    cnt = 1
    for c in arr[idx].down:
        cnt += f(c)

    return cnt

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    e,n = map(int,input().split())
    arr = [Node() for _ in range(e+1)]
    inputs = list(map(int,input().split()))
    for _ in range(0,len(inputs),2):
        start,end = inputs[_], inputs[_+1]
        arr[start-1].down.append(end-1)

    print(f'#{tc}',f(n-1))