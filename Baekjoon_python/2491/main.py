import sys
sys.stdin = open('input.txt', 'r')
##################################################
# def plus(i,n, cnt_up, cnt_dwn, arr):
#     if i == n:
#         return
#     elif i > 0:
#         if arr[i] > arr[i-1]:
#             cnt_up[-1] += 1
#             cnt_dwn.append(1)
#         elif arr[i] < arr[i-1]:
#             cnt_up.append(1)
#             cnt_dwn[-1] += 1
#         else:
#             cnt_up[-1] += 1
#             cnt_dwn[-1] += 1
#
#     plus(i+1, cnt_up, cnt_dwn, arr)


n = int(input())
arr = list(map(int,input().split()))
cnt_up = [1]
cnt_dwn = [1]
i = 1
while i < n:
    if arr[i] > arr[i - 1]:
        cnt_up[-1] += 1
        cnt_dwn.append(1)
    elif arr[i] < arr[i-1]:
        cnt_up.append(1)
        cnt_dwn[-1] += 1
    else:
        cnt_up[-1] += 1
        cnt_dwn[-1] += 1
    i += 1

result = max(max(cnt_up), max(cnt_dwn))
print(result)
