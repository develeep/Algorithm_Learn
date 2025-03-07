import sys
sys.stdin = open('input.txt', 'r')
########################################
# class heap:
#     def __init__(self):
#         self.que = []
#
#     def insert(self, value):
#         self.que.append(value)
#         idx = len(self.que) - 1
#
#         while idx > 0:
#             p = (idx-1) // 2
#             if p >= 0 and self.que[idx] < self.que[p]:
#                 self.que[idx], self.que[p] = self.que[p], self.que[idx]
#                 idx = p
#             else:
#                 break
#

import heapq
T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n, a = map(int,input().split())
    min_heap = []
    max_heap = [-a]
    res = 0
    for _ in range(n):
        x, y = map(int,input().split())
        heapq.heappush(min_heap, x)
        heapq.heappush(max_heap, -y)
        if min_heap[0] < max_heap[0]*-1:
            mi = heapq.heappop(min_heap)
            mx = heapq.heappop(max_heap)*-1
            heapq.heappush(min_heap, mx)
            heapq.heappush(max_heap, -mi)
        res += (max_heap[0]*-1) % 20171109
    print(f'#{tc}', res)