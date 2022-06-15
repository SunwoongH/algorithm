'''
Created by sunwoong on 2022/06/15
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
campus, is_start = [], False
for r in range(n):
    data = list(sys.stdin.readline().rstrip())
    if not is_start:
        for c in range(len(data)):
            if data[c] == 'I':
                is_start = True
                start_r, start_c = r, c
                break
    campus.append(data)
        
def bfs(r: int, c: int) -> int:
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    count = 0
    queue = collections.deque([(r, c)])
    campus[r][c] = 'X'
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and campus[dr][dc] != 'X':
                if campus[dr][dc] == 'P':
                    count += 1
                campus[dr][dc] = 'X'
                queue.append((dr, dc))
    return count
result = bfs(start_r, start_c)
print(result) if result else print('TT')