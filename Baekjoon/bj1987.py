'''
Created by sunwoong on 2022/03/18

>>> Python3로는 시간 초과가 발생하고 PyPy3만 통과되었다. 그리고 문제를 풀면서 의문이 들었던 것은 단순히 상, 하, 좌, 우 탐색 순서만 바꾸었는데
통과 여부의 차이가 발생했던 것이다. 이는 리스트가 메모리에 할당되어 있는 순서에 영향을 받는 것으로 유추되지만 정확한 이유에 대해서는 해결하지 못했다.
문제를 해결하면서 배운 점은 알파벳을 입력받는 과정에서 아스키 코드로 변환 후 check table을 만들어 상수 시간에 방문 여부를 확인할 수 있는 최적화 방법이다.
'''
import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip('\n'))) for _ in range(r)]
check = [False] * 26
result = -sys.maxsize
x = [0, 0, -1, 1]
y = [-1, 1, 0, 0]
def dfs(i: int, j: int, count: int) -> None:
    global result
    result = max(result, count)
    for k in range(4):
        dx, dy = i + x[k], j + y[k]
        if dx >= 0 and dx < r and dy >= 0 and dy < c and not check[board[dx][dy]]:
            check[board[dx][dy]] = True
            dfs(dx, dy, count + 1)
            check[board[dx][dy]] = False
check[board[0][0]] = True
dfs(0, 0, 1)
print(result)