import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque


T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    pizza_arr = list(map(int,input().split()))
    que = deque()
    for i in range(n):
        pizza = pizza_arr[i]
        que.append([pizza, i])
    i += 1
    while len(que) > 0:
        pizza, idx = que.popleft()
        pizza //= 2
        if pizza:
            que.append([pizza,idx])
        else:
            if i < m:
                pizza = pizza_arr[i]
                que.append([pizza, i])
                i += 1
    print(f'#{tc} {idx+1}')
