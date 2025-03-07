import sys
sys.stdin = open('input.txt', 'r')
########################################

def fill(idx):
    global cnt
    l = idx * 2 + 1
    r = idx * 2 + 2
    if idx >= n:
        return
    fill(l)
    arr[idx] += cnt
    cnt += 1
    fill(r)

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    arr = [0]*n
    cnt = 1
    fill(0)
    print(f'#{tc} {arr[0]} {arr[n//2-1]}')