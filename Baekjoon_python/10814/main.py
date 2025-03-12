import sys
sys.stdin = open('input.txt', 'r')
########################################
# 머지소트
def sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = sort(arr[:mid])
    right_arr = sort(arr[mid:])

    sort_arr  = []
    l = r  = 0
    while l < len(left_arr) and r < len(right_arr):
        if int(left_arr[l][0]) <= int(right_arr[r][0]):
            sort_arr.append(left_arr[l])
            l += 1
        else:
            sort_arr.append(right_arr[r])
            r += 1
    sort_arr += left_arr[l:]
    sort_arr += right_arr[r:]
    return sort_arr


n = int(input())
users = [input().split() for _ in range(n)]
# users.sort(key=lambda x:int(x[0]))
res = sort(users)
print('\n'.join([' '.join(user) for user in res]))