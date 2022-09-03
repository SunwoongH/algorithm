'''
Created by sunwoong on 2022/09/03
'''
import sys

n, r, c = map(int, sys.stdin.readline().split())
def divide(n: int, start_r: int, start_c: int, visited: int) -> None:
    if n == 0:
        print(visited)
        return
    if r < start_r + 2 ** (n - 1) and c < start_c + 2 ** (n - 1):
        divide(n - 1, start_r, start_c, visited)
    elif r < start_r + 2 ** (n - 1):
        divide(n - 1, start_r, start_c + 2 ** (n - 1), visited + 2 ** (n - 1) * 2 ** (n - 1))
    elif c < start_c + 2 ** (n - 1):
        divide(n - 1, start_r + 2 ** (n - 1), start_c, visited + (2 ** (n - 1) * 2 ** (n - 1)) * 2)
    else:
        divide(n - 1, start_r + 2 ** (n - 1), start_c + 2 ** (n - 1), visited + (2 ** (n - 1) * 2 ** (n - 1)) * 3)
divide(n, 0, 0, 0)