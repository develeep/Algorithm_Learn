import sys
sys.stdin = open('input.txt', 'r')
###############################################################
import math
# import heapq
def cal_cost(a,b):
    ax,ay = points[a]
    bx,by = points[b]
    if ay == by:
        length = abs(bx - ax)
    elif ax == bx:
        length = abs(by - ay)
    else:
        length = math.sqrt(abs(ax-bx)**2 + abs(ay-by)**2)

    return length**2 * e

class Union:
    def __init__(self):
        self.nodes = list(range(n))

    def find_p(self, v):
        if self.nodes[v] != v:
            self.nodes[v] = self.find_p(self.nodes[v])
        return self.nodes[v]

    def make_union(self, a,b):
        pa,pb = self.find_p(a), self.find_p(b)
        if pa > pb:
            self.nodes[pa] = pb
        else:
            self.nodes[pb] = pa

def f():
    res = 0
    # 크루스칼 알고리즘
    # visited = [0]*n
    # visited[0] = 1

    # q = []
    # for node in range(1,n):
    #     q.append((cal_cost(0,node), node))
    # heapq.heapify(q)
    # while q:
    #     cost, start = heapq.heappop(q)
    #     if visited[start]:
    #         continue
    #     visited[start] = 1
    #     res += cost
    #     for node in range(1,n):
    #         if visited[node] : continue
    #         heapq.heappush(q, (cal_cost(start, node), node))

    # 프림 알고리즘
    ways = []
    for s in range(n):
        for e in range(n):
            if s == e: continue
            ways.append((cal_cost(s,e), s, e))

    ways.sort(key=lambda x:x[0])
    union = Union()
    for cost, a,b in ways:
        pa, pb = union.find_p(a), union.find_p(b)

        if pa != pb:
            union.make_union(pa,pb)
            res += cost

    return res
T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    x_points = tuple(map(int,input().split()))
    y_points = tuple(map(int,input().split()))
    e = float(input())

    points = tuple(zip(x_points,y_points))
    res = f()
    print(f'#{tc} {res:.0f}')