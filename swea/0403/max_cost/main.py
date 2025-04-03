import sys
sys.stdin = open('input.txt', 'r')
###############################################################
def choose_card(idx, arr):
    if len(arr) == 2:
        changes.append(arr)
        return

    for i in range(idx, n):
        choose_card(i+1, arr + [i])


def dfs(cnt):
    global res
    if cnt == m:
        res = max(res, int(''.join(cards)))
        return

    for i in range(len(changes)):
        ca,cb = changes[i]
        cards[ca], cards[cb] = cards[cb], cards[ca]
        if (cnt, tuple(cards)) in used:
            cards[ca], cards[cb] = cards[cb], cards[ca]
            continue
        used.add((cnt, tuple(cards)))
        dfs(cnt + 1)
        cards[ca], cards[cb] = cards[cb], cards[ca]


T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    cards, m = input().split()
    cards = [c for c in cards]
    n = len(cards)
    m = int(m)
    changes = []
    choose_card(0, [])
    used = set()
    res = 0
    dfs(0)
    print(f'#{tc}', res)