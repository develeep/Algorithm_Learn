import sys
sys.stdin = open("input.txt", "r")

###########################################################
def pack_box(carrot_arr, n):
    max_box = n // 2
    result = 1000
    for i in range(1, max_box+1):
        for j in range(i+1,i + max_box + 1):
            a = carrot_arr[:i]
            b = carrot_arr[i:j]
            c = carrot_arr[j:]
            if not(a and b and c):
                continue
            if len(a) > max_box or len(b) > max_box or len(c) > max_box:
                continue
            if a[-1] == b[0] or b[-1] == c[0]:
                continue
            len_box = [len(a), len(b), len(c)]
            result = min(result, max(len_box) - min(len_box))
    return result if result < 1000 else -1


T = int(input())
for test_case in range(1,T + 1):
    n = int(input())
    carrot_arr = sorted(map(int,input().split()))
    result = pack_box(carrot_arr,n)
    print(f'#{test_case} {result}')


