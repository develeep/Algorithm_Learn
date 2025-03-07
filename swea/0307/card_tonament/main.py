import sys
sys.stdin = open('input.txt', 'r')
########################################
dic = {1:3,2:1,3:2}
T = int(input())     # Test case 개수를 받아오는 코드
def check(a,b):
    if cards[a] == cards[b]:
        return a
    if dic[cards[a]] == cards[b]:
        return a
    if dic[cards[b]] == cards[a]:
        return b

def winner(arr):
    if len(arr) == 1:
        return arr[0]

    mid = (len(arr)-1) // 2 + 1
    a = arr[:mid]
    b = arr[mid:]

    a_win = winner(a)
    b_win = winner(b)
    return check(a_win,b_win)

for tc in range(1, T+1):
    n = int(input())
    cards = list(map(int,input().split()))
    player = [i for i in range(n)]
    print(f'#{tc}',winner(player)+1)