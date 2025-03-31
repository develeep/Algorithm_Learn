import sys
sys.stdin = open("input.txt", "r")

###########################################################
def find(x):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if cards[mid] == x:
            return 1
        if cards[mid] > x:
            right = mid
        else:
            left = mid + 1

    return 0

n = int(input())
cards = sorted(list(map(int,input().split())))
m = int(input())
checks = list(map(int,input().split()))
for check in checks:
    print(find(check), end=' ')