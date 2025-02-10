import sys
sys.stdin = open("input.txt", "r")

###########################################################

n, k = map(int,input().split())

arr = [[0,0] for _ in range(6)]
for _ in range(n):
    s, y = map(int,input().split())

    arr[y-1][s] += 1

result = 0

for girl, boy in arr:
    result += girl // k
    result += boy // k
    if girl % k > 0:
        result += 1
    if boy % k > 0:
        result += 1

print(result)
