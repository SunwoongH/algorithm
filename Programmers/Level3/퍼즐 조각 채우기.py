'''
Created by sunwoong on 2025/07/11
'''

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def rotate(board):
    return [list(r)[::-1] for r in zip(*board)]

def dfs(board, visited, r, c, switch, result):
    visited[r][c] = True
    result.append((r, c))
    
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < len(board) and 0 <= dc < len(board[0]):
            if board[dr][dc] == switch and not visited[dr][dc]:
                dfs(board, visited, dr, dc, switch, result)

def solution(game_board, table):
    answer = 0
    empty = []
    shapes = []
    
    visited = [[False for _ in range(len(game_board[0]))] for _ in range(len(game_board))]
    for r in range(len(game_board)):
        for c in range(len(game_board[0])):
            if game_board[r][c] == 0 and not visited[r][c]:
                result = []
                dfs(game_board, visited, r, c, 0, result)
                empty.append(result)
    
    visited = [[False for _ in range(len(table[0]))] for _ in range(len(table))]
    for r in range(len(table)):
        for c in range(len(table[0])):
            if table[r][c] == 1 and not visited[r][c]:
                result = []
                dfs(table, visited, r, c, 1, result)
                shapes.append(result)
                
    used = set()
    
    for i in range(len(shapes)):
        is_promising = False
        
        item = shapes[i]
        
        # shape 라인 계산
        min_r = int(1e9)
        max_r = 0
        min_c = int(1e9)
        max_c = 0
        
        for r, c in item:
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)
        
        shape_row = max_r - min_r + 1
        shape_col = max_c - min_c + 1
        
        # shape 그리기
        shape = [[0 for _ in range(shape_col)] for _ in range(shape_row)]
        for r, c in item:
            shape[r - min_r][c - min_c] = 1
        
        for j in range(len(empty)):
            if j in used:
                continue
            
            item = empty[j]
        
            # empty 라인 계산
            min_r = int(1e9)
            max_r = 0
            min_c = int(1e9)
            max_c = 0
        
            for r, c in item:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
        
            empty_row = max_r - min_r + 1
            empty_col = max_c - min_c + 1
            
            if (shape_row == empty_row and shape_col == empty_col) \
                or (shape_row == empty_col and shape_col == empty_row):
                # empty 그리기
                empty_shape = [[0 for _ in range(empty_col)] for _ in range(empty_row)]
                for r, c in item:
                    empty_shape[r - min_r][c - min_c] = 1
                
                # 90도 상, 하, 좌, 우 확인
                for _ in range(4):
                    is_promising = True
                    
                    if len(shape) != len(empty_shape):
                        is_promising = False
                        empty_shape = rotate(empty_shape)
                        continue
                        
                    for r in range(len(shape)):
                        for c in range(len(shape[0])):
                            shape[r][c] += empty_shape[r][c]
                            
                    for r in range(len(shape)):
                        for c in range(len(shape[0])):
                            if shape[r][c] == 1:
                                is_promising = False
                                break
                        if not is_promising:
                            break
                    
                    for r in range(len(shape)):
                        for c in range(len(shape[0])):
                            shape[r][c] -= empty_shape[r][c]
                    
                    empty_shape = rotate(empty_shape)
                    
                    if is_promising:
                        answer += len(shapes[i])
                        used.add(j)
                        break
            
            if is_promising:
                break
                
    return answer