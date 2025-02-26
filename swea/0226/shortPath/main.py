import sys
sys.stdin = open('input.txt', 'r')
##################################################
import heapq

class Node:
    def __init__(self,index):
        self.index = index
        self.cnt = float('inf')
        self.neighbor = []

    def push_neighbor(self,node,cnt):
        self.neighbor.append((node,cnt))


T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,m,start,end = map(int,input().split())
    arr = [Node(i) for i in range(n)]
    for _ in range(m):
        l,r,cnt = map(int,input().split())
        arr[l-1].push_neighbor(arr[r-1],cnt)
        arr[r-1].push_neighbor(arr[l-1],cnt)

    arr[start-1].cnt = 0
    move_que = []
    heapq.heappush(move_que, (0,arr[start-1]))

    while move_que:
        move_cnt, move_node = heapq.heappop(move_que)
        if move_node == arr[end-1]:
            break
        for node,move in move_node.neighbor:
            move_c = move + move_cnt
            if move_c < node.cnt:
                node.cnt = move_c
                heapq.heappush(move_que, (move_c, node))

    print(f'#{tc}',arr[end-1].cnt)