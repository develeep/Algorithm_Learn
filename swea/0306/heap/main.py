import sys
sys.stdin = open('input.txt', 'r')

class heap_que:
    def __init__(self):
        self.que = []

    def insert(self, value):
        self.que.append(value)
        self.sort()

    def pop(self):
        if len(self.que) == 0:
            return '-1 '
        num = self.que[0]
        self.que[0] = self.que[-1]
        self.que.pop()
        self.sort_pop(0)
        return f'{num} '

    def sort(self):
        i = len(self.que) - 1
        while i >= 0:
            p = (i-1) // 2
            if p >= 0 and self.que[p] < self.que[i]:
                self.que[p], self.que[i] = self.que[i], self.que[p]
                i = p
            else: break

    def sort_pop(self, idx):
        i = idx
        l = 2 * idx + 1
        r = 2 * idx + 2
        if l < len(self.que) and self.que[l] > self.que[i]:
            i = l
        if r < len(self.que) and self.que[r] > self.que[i]:
            i = r
        if i != idx:
            self.que[i], self.que[idx] = self.que[idx], self.que[i]
            self.sort_pop(i)

res = []
T = int(input())  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    heap = heap_que()
    temp = f'#{tc} '
    for _ in range(n):
        inputs = list(map(int, input().split()))
        if inputs[0] == 1:
            heap.insert(inputs[1])
            continue
        if inputs[0] == 2:
            temp += heap.pop()
    res.append(temp)

for i in range(T):
    print(res[i].strip())