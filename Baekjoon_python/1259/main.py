while 1:
    n = input()
    if n == '0':
        break
    elif n == ''.join(reversed(n)):
        print('yes')
    else:
        print('no')

