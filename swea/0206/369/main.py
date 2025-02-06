import sys
sys.stdin = open('input.txt', 'r')
##################################################


n = int(input())
for i in range(1,n+1):
    count = 0
    for s in str(i):
        if s in '369':
            count += 1
    if count:
        print('-'*count, end=" ")
    else:
        print(i, end=" ")