########################################
import sys
sys.stdin = open('input.txt', 'r')

k = int(input())

res = 0
old = []
for _ in range(k):
    n = int(input())
    if n == 0:
        res -= old.pop()
        continue
    res += n
    old.append(n)
print(res)
