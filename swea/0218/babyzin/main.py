import sys
sys.stdin = open('input.txt', 'r')
##################################################
def check_card(arr,):
    count = [0]*10
    result = 1
    for a in arr:
        count[int(a)] += 1
    cnt = 0
    i = 0
    result = 1
    while 1:
        if i == 10:
            break
        if not count[i]:
            i+=1
            continue

        if count[i]:
            cnt += 1

        if i<9 and count[i+1] == 0 or cnt == 3:
            if cnt < 3:
                for j in range(i,i-cnt,-1):
                    if count[j] < 3:
                        result = 0
                        break
            cnt = 0

        i += 1

    return 'true' if result else 'false'

T = int(input())    # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    arr = input().strip()
    result = check_card(arr)
    print(f'#{tc} {result}')
