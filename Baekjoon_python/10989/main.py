import sys
sys.stdin = open("input.txt", "r")

###########################################################
n = int(input())
count = [0]*10001
for _ in range(n):
    i = int(input())
    count[i] += 1
for c in range(1,len(count)):
    if count[c] == 0:
        continue
    for _ in range(count[c]):
        print(c)