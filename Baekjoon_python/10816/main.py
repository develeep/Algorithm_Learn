import sys
sys.stdin = open("input.txt", "r")

###########################################################
def lower_bound(check):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if cards[mid] < check:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(check):
    left = 0
    right = n
    while left < right:
        mid = (left+right) // 2
        if cards[mid] <= check:
            left = mid + 1
        else:
            right = mid
    return right
def binary_find(check):
    l = lower_bound(check)
    r = upper_bound(check)
    return r - l
n = int(input())
cards = list(map(int,input().split()))
cards.sort()
res = []
m = int(input())
checkers = list(map(int,input().split()))
for check in checkers:
    res.append(binary_find(check))

print(' '.join(map(str,res)))