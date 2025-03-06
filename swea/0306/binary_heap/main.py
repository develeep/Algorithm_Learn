import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
class heap:
    def __init__(self):
        self.que = []

    def append(self,value):
        self.que.append(value)
        return self.sort(len(self.que)-1)

    def sort(self,idx):
        parent = (idx-1) // 2
        if parent >= 0 and self.que[idx] < self.que[parent]:
            self.que[idx], self.que[parent] = self.que[parent], self.que[idx]
            self.sort(parent)

    # def bfs(self, m):
    #     q = deque()
    #     if m == self.que[0]:
    #         return 0
    #     q.append((0, 0))
    #     top = len(self.que)-1
    #     while q:
    #         idx, val = q.popleft()
    #         print(idx,val, self.que[idx])
    #         if self.que[idx] == m:
    #             break
    #         l = 2*idx + 1
    #         r = 2*idx + 2
    #         if l <= top:
    #             q.append((l,val + self.que[idx]))
    #         if r <= top:
    #             q.append((r,val + self.que[idx]))
    #     return val

    def cal(self):
        i = len(self.que) -1
        res = 0
        while i > 0:
            parent = (i-1) // 2
            res += self.que[parent]
            i = parent
        return res


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    q = heap()
    for n in nums:
        q.append(n)
    print(f'#{tc}',q.cal())
