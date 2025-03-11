import sys
sys.stdin = open("input.txt", "r")

###########################################################
count = [0]*26
s_arr = [ord(s) for s in input()]

for s in s_arr:
    count[s - 97] +=1

print(' '.join(map(str,count)))
