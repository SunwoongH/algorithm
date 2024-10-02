'''
Created by sunwoong on 2024/10/02
'''
import sys
sys.setrecursionlimit(10 ** 6)

move = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

answer = None

def dfs(n, m, x, y, r, c, k, depth, visited, path):
    visited[x][y][depth] = True
    if depth == k:
        if x == r and y == c:
            global answer
            answer = path
            return
        return
    for oper in move:
        dx = x + oper[1]
        dy = y + oper[2]
        if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy][depth + 1]:
            dfs(n, m, dx, dy, r, c, k, depth + 1, visited, path + oper[0])
        if answer is not None:
            return

def solution(n, m, x, y, r, c, k):
    visited = [[[False for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    dfs(n, m, x - 1, y - 1, r - 1, c - 1, k, 0, visited, "")
    if answer:
        return answer
    return "impossible"

def solution(n, m, x, y, r, c, k):
    distance = abs(x - r) + abs(y - c)
    if distance > k:
        return "impossible"
    elif (k - distance) % 2 != 0:
        return "impossible"
    
    down = max(0, r - x)
    left = max(0, y - c)
    right = max(0, c - y)
    up = max(0, x - r)
    pair = (k - distance) // 2
    
    answer = ''
    for _ in range(k):
        if (down or pair) and x < n:
            answer += 'd'
            x += 1
            if down:
                down -= 1
            else:
                pair -= 1
                up += 1
        elif (left or pair) and y > 1:
            answer += 'l'
            y -= 1
            if left:
                left -= 1
            else:
                pair -= 1
                right += 1
        elif (right or pair) and y < m:
            answer += 'r'
            y += 1
            if right:
                right -= 1
            else:
                pair -= 1
                left += 1
        else:
            answer += 'u'
            x -= 1
            if up:
                up -= 1
            else:
                pair -= 1
                down += 1
    return answer