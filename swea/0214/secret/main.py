import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque
T = 10    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    t = int(input())
    arr = deque(map(int,input().split()))
    flag = 1
    i = 1
    while flag:
        n = arr.popleft() - i
        if n <= 0:
            flag = 0
            n = 0
        arr.append(n)
        i = (i + 1) if i + 1 < 6 else 1
    print(f'#{t}', *arr)