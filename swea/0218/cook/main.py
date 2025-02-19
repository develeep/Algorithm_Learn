import sys
sys.stdin = open('input.txt', 'r')
##################################################

def cook(arr,c,cnt, min_result, index):
    if cnt == len(c)//2:
        cnt1 = []
        cnt2 = []
        for i in range(len(c)):
            if c[i]:
                cnt1.append(i)
            else:
                cnt2.append(i)
        a = 0
        b = 0
        for x in cnt1:
            for y in cnt1:
                a += arr[x][y]
        for x in cnt2:
            for y in cnt2:
                b += arr[x][y]
        min_result[0] = min(min_result[0], abs(a-b))
        return
    cnt += 1
    for i in range(index,len(c)-(len(c)//2-cnt)):
        c[i] = 1
        cook(arr,c,cnt,min_result,i+1)
        c[i] = 0

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    i = 0
    c = [0]*n
    c[0] = 1
    cnt = 1
    min_result = [float('inf')]
    cook(arr, c,cnt, min_result,1)
    print(f'#{tc}',min_result[0])