import sys
sys.stdin = open("input.txt", "r")

###########################################################
n = int(input())

arr = sorted([list(map(int,input().split())) for _ in range(n)], key = lambda x: x[0])
zip_arr = list(zip(*arr))
max_h = max(zip_arr[1])
max_idx = zip_arr[1].index(max_h)
result = 0

i = 0
while i < max_idx:
    for j in range(i+1, max_idx + 1):
        if arr[j][1] > arr[i][1] or arr[j][1] == max_h:
            result += arr[i][1] * (arr[j][0] - arr[i][0])
            i = j
            break
result += max_h
next_arr = zip_arr[1][i + 1:]
if next_arr:
    max_h = max(next_arr)
    max_idx = i + next_arr.index(max_h) + 1

while i < n - 1:
    for j in range(i+1,n):
        if arr[j][1] == max_h:
            result += max_h * (arr[j][0] - arr[i][0])
            if j + 1 == n:
                i = j
                break
            next_arr = zip_arr[1][j + 1:]
            max_h = max(next_arr)
            max_idx = j + next_arr.index(max_h) + 1
            i = j
            break
print(result)