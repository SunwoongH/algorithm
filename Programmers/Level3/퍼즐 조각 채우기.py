'''
Created by sunwoong on 2025/07/10
'''

move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def rotate(board):
    return [list(r)[::-1] for r in zip(*board)]

def dfs(board, r, c, case, visited, result):
    visited[r][c] = True
    result.append((r, c))
    
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < len(board) and 0 <= dc < len(board[0]) and board[dr][dc] == case and not visited[dr][dc]:
            dfs(board, dr, dc, case, visited, result)

def solution(game_board, table):
    empty = []
    full = []
    used = set()
    answer = 0
    
    visited = [[False for _ in range(len(game_board[0]))] for _ in range(len(game_board))]
    for r in range(len(game_board)):
        for c in range(len(game_board[0])):
            if game_board[r][c] == 0 and not visited[r][c]:
                result = []
                dfs(game_board, r, c, 0, visited, result)
                empty.append(result)
    
    visited = [[False for _ in range(len(table[0]))] for _ in range(len(table))]
    for r in range(len(table)):
        for c in range(len(table[0])):
            if table[r][c] == 1 and not visited[r][c]:
                result = []
                dfs(table, r, c, 1, visited, result)
                full.append(result)
    
    print(empty)
                
    for i in range(len(full)):
        item = full[i]
        min_r = int(1e9)
        max_r = 0
        min_c = int(1e9)
        max_c = 0
        for r, c in item:
            print(r, c)
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)
        line = max(max_r - min_r, max_c - min_c) + 1
        
        board = [[0 for _ in range(line)] for _ in range(line)]
        
        for r, c in item:
            board[r - min_r][c - min_c] = 1
        print(min_r, min_c)
        for t in board:
            print(t)
            
        for j in range(len(empty)):
            is_promising = True
            item = empty[j]
            min_r = int(1e9)
            max_r = 0
            min_c = int(1e9)
            max_c = 0
            for r, c in item:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
            empty_line = max(max_r - min_r, max_c - min_c) + 1
            
            if j not in used and line == empty_line:
                temp = [[0 for _ in range(line)] for _ in range(line)]
                for r, c in item:
                    temp[r - min_r][c - min_c] = 1
                for _ in range(4):
                    is_promising = True
                    print()
                    print(i, j)
                    
                    for t in board:
                        print(t)
                    print()

                    for r in range(line):
                        for c in range(line):
                            board[r][c] += temp[r][c]
                            
                    for r in range(line):
                        for c in range(line):
                            if board[r][c] == 1:
                                is_promising = False
                                break
                        if not is_promising:
                            break

                    for t in board:
                        print(t)
                        
                    print()
                    for t in temp:
                        print(t)
                    
                    for r in range(line):
                        for c in range(line):
                            board[r][c] -= temp[r][c]
                            
                    temp = rotate(temp)
                    
                    if is_promising:
                        answer += len(item)
                        used.add(j)
                        break
                        
                if is_promising:
                    break
        
    return answer