import sys

n = int(sys.stdin.readline())

result = []
num = 2
while n != 1 and num <= int(n ** 0.5):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if not prime: num += 1
    else:
        if n % num == 0:
            result.append(num)
            n //= num
            prime = True
            for i in range(2, n):
                if n % i == 0:
                    prime = False
            if prime:
                result.append(n)
                break
        else: num += 1

if len(result) == 0: print(n)
else:
    for r in result:
        print(r)