import sys
sys.stdin = open("input.txt", "r")

###########################################################

arr = [int(input()) for _ in range(9)]
arr.sort()
hap = sum(arr)
cha = hap - 100
flag = False

for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i] + arr[j] == cha:
            arr.pop(i)
            arr.pop(j-1)
            flag = True
            break
    if flag:
        break
print(*arr,sep='\n')