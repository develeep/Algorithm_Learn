import sys
sys.stdin = open('input.txt', 'r')
##################################################

n, k = map(int,input().split())

arr = list(map(int,input().split()))


hap = 0
for i in range(k):
    hap += arr[i]
max_result = hap

for i in range(k,n):
    hap -= arr[i-k]
    hap += arr[i]
    max_result = max(max_result, hap)

print(max_result)
