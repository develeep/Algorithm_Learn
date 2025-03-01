import sys
sys.stdin = open("input.txt", "r")

###########################################################

def f(arr):
    if len(arr) == 6:
        print(' '.join(map(str,arr)))
        return

    for i in range(k):
        if visited[i] or arr and arr[-1] > s_num[i]:
            continue
        visited[i] = 1
        f(arr+[s_num[i]])
        visited[i] = 0

while True:
    try:
        k, *s_num = list(map(int, input().split()))
        visited = [0] * k
        f([])
        print()
    except EOFError:
        break

