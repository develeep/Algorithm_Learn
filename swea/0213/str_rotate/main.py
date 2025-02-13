import sys
sys.stdin = open('input.txt', 'r')
##################################################

n = int(input())
arr = [input() for _ in range(n)]

def reverse_str(str, i):
    if i == 0:
        return str[i]
    return str[i] + reverse_str(str, i-1)

for s in arr:
    print(reverse_str(s,len(s)-1))