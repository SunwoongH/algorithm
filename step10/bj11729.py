def hanoi(num, From, temp, to, result):
    if num == 1:
        result.append([From, to])
        return
    else:
        hanoi(num - 1, From, to, temp, result)
        result.append([From, to])
        hanoi(num - 1, temp, From, to, result)

n = int(input())
result = []
hanoi(n, 1, 2, 3, result)
print(len(result))
for v in result:
    print(v[0], v[1])