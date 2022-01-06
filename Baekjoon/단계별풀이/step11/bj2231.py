import sys

n = int(sys.stdin.readline())
check = False
for i in range(1, n):
    sum_num = i
    sum_num += sum(list(map(int, str(i))))
    if sum_num == n:
        check = True
        print(i)
        break
if not check:
    print(0)