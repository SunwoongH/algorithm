n = int(input())
if n < 10:
    n *= 10

temp = n
count = 0
while True:
    n = (n % 10 * 10) + (((n // 10) % 10 + n % 10) % 10)
    count += 1
    if n == temp:
         break
print(count)