import sys
sys.stdin = open('input.txt', 'r')
###############################################################
two_dic = {0 : 1,1 : 0}
three_dic = {0 : (1,2),1 : (0,2),2 : (0,1)}

def cal_two(nums):
    c = 1
    res = 0
    for num in reversed(nums):
        res += num * c
        c *= 2
    return res

def cal_three(nums):
    c = 1
    res = 0
    for num in reversed(nums):
        res += num * c
        c *= 3
    return res

def f():
    for i in range(len(two)):
        for j in range(len(three)):
            old_n = three[j]
            for n in three_dic[three[j]]:
                two[i] = two_dic[two[i]]
                two_res = cal_two(two)
                two[i] = two_dic[two[i]]
                three[j] = n
                three_res = cal_three(three)
                three[j] = old_n
                if two_res == three_res:
                    return two_res
T = int(input())    #test case 개수를 받아오는 코드
for tc in range(1, T+1):
    two = [int(s) for s in input()]
    three = [int(s) for s in input()]
    print(f'#{tc}', f())