import sys
sys.stdin = open('input.txt', 'r')
##################################################

n = int(input())
switch_arr = list(map(int,input().split()))
student = int(input())
student_arr = [list(map(int,input().split())) for _ in range(student)]

for sex, index in student_arr:
    if sex == 1:
        for i in range(index-1,len(switch_arr), index):
            switch_arr[i] = int(switch_arr[i] != 1)
        continue
    switch_arr[index-1] = int(switch_arr[index-1] != 1)
    for i in range(1, len(switch_arr)-index+1):
        big_index = index + i - 1
        small_index = index - i - 1
        if small_index >= 0 and big_index < len(switch_arr) and switch_arr[small_index] == switch_arr[big_index]:
            switch_arr[small_index] = int(switch_arr[small_index] != 1)
            switch_arr[big_index] = int(switch_arr[big_index] != 1)
        else:
            break

for i in range(0,len(switch_arr),20):
    print(*switch_arr[i:i+20])

