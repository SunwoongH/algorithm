import sys

m, n = map(int, sys.stdin.readline().split())
nums = list([True for _ in range(m, n + 1)])

for i in range(2, int(n ** 0.5) + 1):
    if m // i == 0 or m == i:
        start = i
        if nums[start - m] == True:
            for j in range(start * 2, n + 1, i):
                nums[j - m] = False
    elif m % i == 0:
        start = i * (m // i)
        for j in range(start, n + 1, i):
            nums[j - m] = False
    else: 
        start = i * ((m // i) + 1)
        for j in range(start, n + 1, i):
            nums[j - m] = False
if m == 1:
    for i in range(1, len(nums)):
        if nums[i] == True: print(i + m)
else:
    for i in range(len(nums)):
        if nums[i] == True: print(i + m)