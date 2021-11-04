import sys

def fibonacci(n):
    fib = [[0, 0] for _ in range(n + 1)]
    fib[0][0] = 1
    fib[0][1] = 0
    if n == 0: return fib[0][0], fib[0][1]
    fib[1][0] = 0
    fib[1][1] = 1
    if n == 1: return fib[1][0], fib[1][1]
    else:
        for i in range(2, n + 1):
            fib[i][0] = fib[i - 1][0] + fib[i - 2][0]
            fib[i][1] = fib[i - 1][1] + fib[i - 2][1]
    return fib[n][0], fib[n][1]
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    zero, one = fibonacci(n)
    print(zero, one)