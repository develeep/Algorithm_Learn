from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')
##################################################


x,y = map(int,input().split())
n = int(input())
question_arr = [list(map(int,input().split())) for _ in range(n)]
x_cuts = [0]
y_cuts = [0]
for d, index in question_arr:
    if d:
        x_cuts.append(index)
    else:
        y_cuts.append(index)

x_cuts.append(x)
y_cuts.append(y)
x_cuts.sort()
y_cuts.sort()

max_x = 0
for i in range(1,len(x_cuts)):
    cha_x = x_cuts[i] - x_cuts[i-1]
    max_x = max(max_x, cha_x)

max_y = 0
for j in range(1,len(y_cuts)):
    cha_y = y_cuts[j] - y_cuts[j-1]
    max_y = max(max_y, cha_y)

print(max_x * max_y)