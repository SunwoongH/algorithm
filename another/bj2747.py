num = int(input())
a = [0] * (num + 1)
a[1] = 1
for i in range(2, num + 1):
    a[i] = a[i - 1] + a[i - 2]
print(a[num])