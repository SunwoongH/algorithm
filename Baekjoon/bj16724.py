'''
Created by sunwoong 2025/05/01
'''
import sys

n, m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    line = list(sys.stdin.readline().rstrip())
    maps.append(line)

move = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}

sequence = 1
for r in range(n):
    for c in range(m):
        if maps[r][c] in ('D', 'L', 'R', 'U'):
            seen = set()
            sr, sc = r, c
            case = 1
            temp = None
            while True:
                pos = move[maps[sr][sc]]
                seen.add((sr, sc))
                dr, dc = pos[0] + sr, pos[1] + sc
                if (dr, dc) in seen:
                    break
                if dr < 0 or dr >= n or dc < 0 or dc >= m:
                    break
                if not maps[dr][dc] in ('D', 'L', 'R', 'U'):
                    case = 2
                    temp = maps[dr][dc]
                    break
                sr, sc = dr, dc
            if case == 1:
                for item in seen:
                    maps[item[0]][item[1]] = sequence
                sequence += 1
            if case == 2:
                for item in seen:
                    maps[item[0]][item[1]] = temp

print(sequence - 1)