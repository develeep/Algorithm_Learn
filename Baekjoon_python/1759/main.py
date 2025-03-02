import sys
sys.stdin = open('input.txt','r')

l,c = map(int,input().split())
str_arr = sorted(input().split())
m = ['a','e','i','o','u']
def dfs(idx, arr, special,nomal):
    if len(arr) == l:
        print(''.join(map(str, arr)))
        return

    for i in range(idx,c):
        if str_arr[i] in m:
            if l - special <= 2:
                continue
            dfs(i+1,arr+[str_arr[i]],special+1,nomal)
        else:
            if nomal >= l-1:
                continue
            dfs(i+1,arr+[str_arr[i]],special,nomal+1)

dfs(0,[],0,0)