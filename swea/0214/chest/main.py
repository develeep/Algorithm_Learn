import sys
sys.stdin = open('input.txt', 'r')
##################################################
from collections import deque

def makeNum(arr,r):
    if r == 0:
        return ''
    n = arr[0]
    arr.rotate(-1)
    return n + makeNum(arr, r-1)

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,k = map(int,input().split())
    arr = deque([s for s in input()])
    nums = set()
    rotate = n // 4
    for _ in range(rotate):
        for _ in range(4):
            # num = ''
            # for i in range(rotat::):
            #     num += arr[0]
            #     arr.rotate(-1)
            num = makeNum(arr,rotate)
            nums.add(int(num, 16))
        arr.rotate(-1)

    sorted_nums = sorted(nums, reverse=True)
    print(f'#{tc} {sorted_nums[k-1]}')