'''
Created by sunwoong on 2023/04/12
'''
import sys
input = sys.stdin.readline

def floyd():
    for l in range(n):
        for r in range(n):
            for c in range(n):
                board[r][c] = min(board[r][c], board[r][l] + board[l][c])

def dfs(r, depth, time):
    if depth == n:
        global answer
        answer = min(answer, time)
        return
    for c in range(n):
        if c != r and not visited[c]:
            visited[c] = True
            dfs(c, depth + 1, time + board[r][c])
            visited[c] = False

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize
visited = [False for _ in range(n)]
floyd()
visited[k] = True
dfs(k, 1, 0)
print(answer)