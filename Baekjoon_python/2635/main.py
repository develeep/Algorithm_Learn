n = int(input())
def find_count(a,b):
    if a-b < 0:
        return [a,b]
    return [a, *find_count(b,a-b)]

result = 1
result_arr = [0]
for i in range(n,0,-1):
    count = find_count(n,i)
    if result < len(count):
        result = len(count)
        result_arr = count
print(result)
print(*result_arr)