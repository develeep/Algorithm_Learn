import sys
sys.stdin = open('input.txt', 'r')
########################################
def hanoi(n, start, mid, end):
    global history
    if n == 1:
        history.append(f'{start} {end}')
        return

    hanoi(n-1, start, end, mid)

    history.append(f'{start} {end}')

    hanoi(n-1, mid, start, end)

n = int(input())
history = []
hanoi(n,1,2,3)
print(len(history))
print('\n'.join(history))