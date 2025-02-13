import sys
sys.stdin = open("input.txt", "r")

###########################################################
p,q = map(int,input().split())
w,h = map(int,input().split())
t = int(input())
dw = [1,-1,-1,1]
dh = [1,1,-1,-1]
direction = 0
i = 0
while 1:
    nw = w + (p - 2 * w) * (dw[direction] > 0)
    nh = h + (q - 2 * h) * (dh[direction] > 0)
    print(w,h)
    if t - i < nw and t - i < nh:
        w = w + dw[direction] * (t - i)
        h = h + dh[direction] * (t - i)
        break

    if nw < nh:
        w += dw[direction] * nw
        h += + dh[direction] * nw
        if direction < 2:
            direction = 0 if direction else 1
        else:
            direction = 3 if direction == 2 else 2
        i += nw
        continue
    if nw == nh:
        w += dw[direction] * nw
        h += + dh[direction] * nw
        direction = (direction + 2) % 4
        i += nw
        continue
    if nw > nh:
        w += dw[direction] * nh
        h += + dh[direction] * nh
        if direction % 3 == 0:
            direction = 0 if direction else 3
        else:
            direction = 2 if direction == 1 else 1
        i += nh
        continue
    break
print(w,h)