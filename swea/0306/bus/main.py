import sys
sys.stdin = open('input.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    cnt = [0]*5000
    for _ in range(n):
        a,b = map(int,input().split())
        for i in range(a-1,b):
            cnt[i] += 1
    p = int(input())
    res = []
    for _ in range(p):
        c = int(input())
        res.append(cnt[c-1])

    print(f'#{tc}',' '.join(map(str,res)))