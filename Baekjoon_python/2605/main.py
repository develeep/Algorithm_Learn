import sys
sys.stdin = open("input.txt", "r")

###########################################################

n = int(input())
arr = list(map(int,input().split()))
result = []
for i in range(n):
    result.insert(-arr[i] if arr[i] else i, i+1)
print(*result)
