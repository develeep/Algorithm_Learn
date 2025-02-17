import sys
sys.stdin = open("input.txt", "r")

###########################################################

n = int(input())
paper_arr = [list(map(int,input().split())) for _ in range(n)]
arr = [[0] * 1001 for _ in range(1001)]
cnt_result = [0] * n

for idx in range(n-1,-1,-1):
    paper = paper_arr[idx]
    cnt = 0
    for i in range(paper[1], paper[1]+paper[3]):
        for j in range(paper[0], paper[0]+paper[2]):
            if arr[i][j]:
                continue
            cnt_result[idx] += 1
            arr[i][j] = 1
print(*cnt_result,sep='\n')

