import sys
sys.stdin = open('input.txt', 'r')
##################################################
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
def check(n,k,new_arr,index,cnt):
    if len(new_arr) == n:
        if sum(new_arr) == k:
            cnt[0] += 1
        return
    for i in range(index,len(arr)):
        check(n,k,new_arr+[arr[i]],i+1,cnt)

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n,k = map(int,input().split())
    cnt = [0]
    check(n,k,[],0,cnt)
    print(f'#{tc}',cnt[0])