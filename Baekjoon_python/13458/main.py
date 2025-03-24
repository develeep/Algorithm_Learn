import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int,input().split()))
b,c = map(int,input().split())

cnt = 0
for p in arr:
    cnt += 1 + (p>b) * ((p-b) // c) + (1 * (p-b > 0 and (p-b) % c > 0))
print(cnt)