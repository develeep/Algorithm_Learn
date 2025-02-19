import sys
sys.stdin = open('input.txt', 'r')
##################################################
def check_card(arr):
    count = [0]*10
    for index in range(len(arr)):
        a = arr[index]
        count[a] += 1
        if index > 1:
            a1 = a2 = a3 = []
            if count[a] == 3:
                return ['t', index*2]
            if a > 2 and a+1 < 11:
                a1 = count[a-2:a+1]
            if a > 1 and a+2 < 11:
                a2 = count[a-1:a+2]
            if a+3 < 11:
                a3 = count[a:a+3]
            if (a1 and not a1.count(0)) or (a2 and not a2.count(0)) or (a3 and not a3.count(0)):
                return ['r', index*2]


T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    arr = list(map(int,input().split()))
    x1 = []
    x2 = []
    for i in range(len(arr)):
        if i%2 == 0:
            x1.append(arr[i])
        else:
            x2.append(arr[i])
    print(f'#{tc}', end=' ')
    x1_result = check_card(x1)
    x2_result = check_card(x2)
    if x1_result and x2_result:
        if x2_result:
            x2_result[1] += 1
        if(x1_result[1] - x2_result[1]) > 0:
            print(2)
        else:
            print(1)
    else:
        if x1_result:
            print(1)
        elif x2_result:
            print(2)
        else:
            print(0)
