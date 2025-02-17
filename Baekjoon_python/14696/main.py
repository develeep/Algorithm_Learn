import sys
sys.stdin = open('input.txt','r')

n = int(input())

for _ in range(n):
    cntA = [0, 0, 0, 0]
    cntB = [0, 0, 0, 0]
    a_cnt, *a_cards = list(map(int,input().split()))
    b_cnt, *b_cards = list(map(int,input().split()))
    for i in range(a_cnt):
        cntA[a_cards[i]-1] += 1
    for i in range(b_cnt):
        cntB[b_cards[i]-1] += 1
    result = 'D'
    for c in range(3,-1,-1):
        if cntA[c] > cntB[c]:
            result = 'A'
            break
        elif cntA[c] < cntB[c]:
            result = 'B'
            break

    print(result)