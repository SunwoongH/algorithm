n = int(input())

def fibonacci(num):
    if num <= 1:
        return num
    ppreN = 0
    preN = 1
    for i in range(2, num + 1):
        result = ppreN + preN
        ppreN = preN
        preN = result
    return result

print(fibonacci(n))