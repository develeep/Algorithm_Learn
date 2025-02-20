import sys
sys.stdin = open('input.txt', 'r')
##################################################
T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, m = map(int,input().split())
    container = sorted(map(int,input().split()))
    truck = sorted(map(int,input().split()))

    weight = 0
    while truck and container:
        t = truck.pop()
        while container:
            c = container.pop()
            if c <= t:
                weight += c
                break
    print(f'#{tc} {weight}')
