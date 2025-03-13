import sys
sys.stdin = open('input.txt', 'r')
########################################
def sort(arr):
    global c
    if len(arr) < 2:
        return arr

    m = len(arr) // 2
    left = sort(arr[:m])
    right = sort(arr[m:])
    l = r = 0
    res = []
    if left[-1] > right[-1]:
        c += 1
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += left[l:]
    res += right[r:]

    return res


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int,input().split()))
    c = 0
    result = sort(nums)
    print(f'#{tc}', result[n//2], c)