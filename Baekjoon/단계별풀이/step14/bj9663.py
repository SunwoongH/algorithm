'''
문제 - N-Queen

풀이 방법 - 재귀 구조 DFS로 풀이

>>> pypy3로는 통과가 되었지만 python3로는 시간 초과가 발생하였다.
'''
import sys

n = int(sys.stdin.readline())
columns = [-sys.maxsize for _ in range(n)]
visited = [False for _ in range(n)]
count = 0
def queens(row):
    global count
    if row == n:
        count += 1
        return
    for column in range(n):
        if visited[column] == 0:
            check = False
            for i, j in enumerate(columns[:row]):
                if abs(column - j) == row - i:
                    check = True
                    break
            if not check:
                columns[row] = column
                visited[column] = True
                queens(row + 1)
                visited[column] = False
queens(0)
print(count)