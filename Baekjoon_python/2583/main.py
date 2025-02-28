import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque

n,m,k = map(int,input().split())
count_x = [0]*n
count_y = [0]*k
for _ in range(k):
