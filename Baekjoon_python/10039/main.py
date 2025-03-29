import sys
sys.stdin = open('input.txt', 'r')

sum_num = 0
for _ in range(5):
    num = int(input())
    sum_num += num if num >= 40 else 40

print(sum_num//5)