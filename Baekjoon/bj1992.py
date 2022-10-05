'''
Created by sunwoong on 2022/10/05
'''
import sys

def compression(n: int, start_r: int, start_c: int) -> str:
    if n == 1:
        return image[start_r][start_c]
    required = False
    target = image[start_r][start_c]
    for r in range(start_r, start_r + n):
        for c in range(start_c, start_c + n):
            if image[r][c] != target:
                required = True
                break
    if required:
        expression = '('
        expression += compression(n // 2, start_r, start_c)
        expression += compression(n // 2, start_r, start_c + n // 2)
        expression += compression(n // 2, start_r + n // 2, start_c)
        expression += compression(n // 2, start_r + n // 2, start_c + n // 2)
        expression += ')'
        return expression
    else:
        return target

n = int(sys.stdin.readline())
image = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
print(compression(n, 0, 0))