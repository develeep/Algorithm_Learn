total = 21
count = [0]
que = [1]
result = 1
i = 1
while total > 0:
    print('count=', count)
    print('que=', que)

    for _ in range(len(que)):
        print(que)
        i = que.pop()
        count[i-1] += 1
        if total < count[i-1]:
            total = 0
            break
        total -= count[i-1]
        result = i
        print(total)
    count.append(0)
    print()
    for i in range(len(count)):
        que.append(i+1)

print(result)
