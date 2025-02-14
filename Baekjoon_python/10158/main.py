import sys
sys.stdin = open("input.txt", "r")

###########################################################
p,q = map(int,input().split())
w,h = map(int,input().split())
t = int(input())

w_count = (w + t) // p
h_count = (h + t) // q

x,y = 0,0

if w_count % 2 == 0:
    x = (w + t) % p
else:
    x = p - (w + t) % p

if h_count % 2 == 0:
    y = (h + t) % q
else:
    y = q - (h + t) % q

print(x,y)