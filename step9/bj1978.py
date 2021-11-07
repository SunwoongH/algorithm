import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = 0
for num in nums:
    check = True
    if num == 1:
        check = False
    else:
        for i in range(2, num):
            if num % i == 0:
                check = False
                break
    if check: count += 1
print(count)
