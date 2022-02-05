a = int(input())
b = int(input())
c = int(input())

num = list(str(a * b * c))
digits = [0] * 10

for i in num:
    digits[int(i)] += 1

for i in digits:
    print(i)