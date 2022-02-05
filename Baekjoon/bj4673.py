def selfNumCheck(num):
    temp = list(str(num))
    result = num
    for i in temp:
        result += int(i)
    return result

nums = []
for i in range(1, 10001):
    nums.append(selfNumCheck(i))

for i in range(1, 10001):
    check = 0
    for num in nums:
        if num == i:
            check = 1
            break
    if check == 0:
        print(i)
