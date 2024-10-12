'''
Created by sunwoong on 2024/10/12
'''
from itertools import permutations
from collections import defaultdict, deque
import sys

cards = defaultdict(list)
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(s_r, s_c, e_r, e_c, board):
    visited = [[False for _ in range(len(board))] for _ in range(len(board))]
    queue = deque([(s_r, s_c, 0)])
    while queue:
        r, c, cost = queue.popleft()
        if e_r == r and e_c == c:
            return cost
        
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < len(board) and 0 <= dc < len(board) and not visited[dr][dc]:
                visited[dr][dc] = True
                queue.append((dr, dc, cost + 1))
            cr = r
            cc = c
            while True:
                dr = cr + oper[0]
                dc = cc + oper[1]
                if not (0 <= dr < len(board) and 0 <= dc < len(board)):
                    if not (cr == r and cc == c):
                        if not visited[cr][cc]:
                            visited[cr][cc] = True
                            queue.append((cr, cc, cost + 1))
                    break
                if board[dr][dc] != 0:
                    if not visited[dr][dc]:
                        visited[dr][dc] == True
                        queue.append((dr, dc, cost + 1))
                    break
                cr, cc = dr, dc
    return 0

def calculate_path(s_r, s_c, pos, path, board):
    if pos == len(path):
        return 0
    card = cards[path[pos]]
    
    left = 2
    left += bfs(s_r, s_c, card[0][0], card[0][1], board)
    board[card[0][0]][card[0][1]] -= path[pos]
    left += bfs(card[0][0], card[0][1], card[1][0], card[1][1], board)
    board[card[1][0]][card[1][1]] -= path[pos]
    left += calculate_path(card[1][0], card[1][1], pos + 1, path, board)
    board[card[0][0]][card[0][1]] += path[pos]
    board[card[1][0]][card[1][1]] += path[pos]
    
    right = 2
    right += bfs(s_r, s_c, card[1][0], card[1][1], board)
    board[card[1][0]][card[1][1]] -= path[pos]
    right += bfs(card[1][0], card[1][1], card[0][0], card[0][1], board)
    board[card[0][0]][card[0][1]] -= path[pos]
    right += calculate_path(card[0][0], card[0][1], pos + 1, path, board)
    board[card[0][0]][card[0][1]] += path[pos]
    board[card[1][0]][card[1][1]] += path[pos]
    
    return min(left, right)

def solution(board, r, c):
    answer = sys.maxsize
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                cards[board[i][j]].append((i, j))
                
    for case in permutations(cards.keys(), len(cards.keys())):
        answer = min(answer, calculate_path(r, c, 0, case, board))
    
    return answer