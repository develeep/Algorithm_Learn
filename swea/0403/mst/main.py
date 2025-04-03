import sys
sys.stdin = open('input.txt', 'r')
###############################################################
class Union:
    def __init__(self, l):
        self.nodes = list(range(l+1))

    def find_p(self, v):
        if self.nodes[v] != v:
            self.nodes[v] = self.find_p(self.nodes[v])
        return self.nodes[v]

    def set_union(self,a,b):
        pa = self.find_p(a)
        pb = self.find_p(b)

        if pa > pb:
            self.nodes[pa] = pb
        else:
            self.nodes[pb] = pa


T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n,m = map(int,input().split())
    edges = sorted([tuple(map(int,input().split())) for _ in range(m)], key=lambda x : x[2])
    union = Union(n)
    res = 0
    for s,e,w in edges:
        ps = union.find_p(s)
        pe = union.find_p(e)
        if ps != pe:
            union.set_union(ps,pe)
            res += w
    print(f'#{tc}', res)