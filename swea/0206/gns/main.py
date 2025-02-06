import sys

sys.stdin = open('input.txt', 'r')
##################################################
NUM = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9,
}

key = list(NUM.keys())

T = int(input())  # Testcase 개수를 받아오는 코드
for tc in range(1, T + 1):
    t, length = input().split()
    str_arr = input().split()
    arr = []
    result = [0] * len(str_arr)
    count = [0] * 10

    for s in str_arr:
        n = NUM[s]
        count[n] += 1

    for idx in range(1, len(count)):
        count[idx] += count[idx-1]

    for idx in range(len(str_arr)-1, -1, -1):
        n = NUM[str_arr[idx]]
        result[count[n]-1] = str_arr[idx]
        count[n] -= 1

    print(t)
    print(' '.join(result))
