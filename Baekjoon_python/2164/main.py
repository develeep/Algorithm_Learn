import sys
sys.stdin = open('input.txt', 'r')
########################################
from collections import deque
n = int(input())
cards = [i for i in range(1,n+1)]
q = deque(cards)
while len(q) > 1:
    trash = q.popleft()
    card = q.popleft()
    q.append(card)

print(q[0])