import sys
sys.stdin = open('input.txt', 'r')
##################################################
import heapq

# class Node:
#     def __init__(self,index):
#         self.index = index
#         self.cnt = float('inf')
#         self.neighbor = []
#
#     def push_neighbor(self,node,cnt):
#         self.neighbor.append((node,cnt))

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,m,start,end = map(int,input().split())
    # arr = [Node(i) for i in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        l, r, cnt = map(int,input().split())
        graph[l-1].append((r-1, cnt))
        graph[r-1].append((l-1, cnt))

    min_cnt = [float('inf')]*n
    min_cnt[start-1] = 0
    move_que = []
    heapq.heappush(move_que, (0, start-1))

    while move_que:
        move_cnt, move_idx = heapq.heappop(move_que)
        if move_idx == end-1:
            break
        for index, cnt in graph[move_idx]:
            move = cnt + move_cnt
            if move < min_cnt[index]:
                min_cnt[index] = move
                heapq.heappush(move_que,(move, index))

    print(f'#{tc}', min_cnt[end-1])