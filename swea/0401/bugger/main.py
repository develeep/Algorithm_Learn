def dfs(idx, kal, res):
    global max_result
    if idx == n:
        max_result = max(max_result, res)
        return

    if (kal + foods[idx][1]) <= l:
        dfs(idx + 1, kal + foods[idx][1], res + foods[idx][0])

    dfs(idx + 1, kal, res)


T = int(input())  # test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    n, l = map(int, input().split())
    foods = [tuple(map(int, input().split())) for _ in range(n)]
    max_result = 0
    dfs(0, 0, 0)
    print(f'#{tc}', max_result)