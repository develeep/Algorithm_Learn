import sys

sys.stdin = open('input.txt', 'r')

n = int(input())
nums = list(map(int, input().split()))


def find(number):
    if number < 2:
        return 0
    i = 2
    while i**2 <= number:
        if number % i == 0:
            return 0
        i += 1
    return 1


result = 0
for num in nums:
    result += find(num)

print(result)
