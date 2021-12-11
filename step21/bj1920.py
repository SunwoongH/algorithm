import sys

def binary_search(a, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if key > a[mid]: low = mid + 1
        elif key < a[mid]: high = mid - 1
        else:
            print('1')
            return
    print('0')

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
num_of_m = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
a = sorted(a)
for i in range(num_of_m):
    binary_search(a, 0, n - 1, m[i])