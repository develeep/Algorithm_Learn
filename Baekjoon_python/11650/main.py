import sys
sys.stdin = open('input.txt', 'r')
########################################
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort()

print('\n'.join(map(lambda x: ' '.join(map(str,x)), arr)))