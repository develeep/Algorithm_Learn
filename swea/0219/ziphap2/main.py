import sys
sys.stdin = open('input.txt', 'r')
##################################################
def check(new_arr,arr,index,cnt):
    if sum(new_arr) == 0:
        cnt[0] = 1
    if len(new_arr) == 10:
        return
    for i in range(index,10):
        check(new_arr+[arr[i]],arr,i+1,cnt)

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    arr = list(map(int,input().split()))
    print(arr)
    cnt = [0]
    check([],arr,0,cnt)
    print(f'#{tc}',cnt[0])