import sys
sys.stdin = open('input.txt', 'r')
##################################################
def find(arr,n):
    for h in range(n):
        for w in range(n):
            if arr[h][w]:
                for d in range(4):
                    for cnt in range(1,5):
                        nw = w + dw[d] * cnt
                        nh = h + dh[d] * cnt
                        if not (0 <= nw < n and 0 <= nh < n and arr[nh][nw]):
                            break
                    else:
                        return True
    return False
dir = {'.': 0, 'o': 1}


T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n = int(input())
    arr = [[dir[s] for s in input()] for _ in range(n)]
    dw = [1,0,1,-1]
    dh = [0,1,1,1]
    print(f"#{tc} {'YES' if find(arr,n) else 'NO'}")