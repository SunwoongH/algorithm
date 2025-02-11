'''
Created by sunwoong on 2025/02/11
'''

from itertools import product

answer = int(1e9)
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def backtracking(maze, red, blue, count, red_visited, blue_visited):
    if maze[red[0]][red[1]] == 3 and maze[blue[0]][blue[1]] == 4:
        global answer
        answer = min(answer, count)
        return
    if count > answer:
        return

    for red_move, blue_move in product(move, repeat=2):
        d_red = d_blue = None
        
        if maze[red[0]][red[1]] != 3:
            d_red = (red[0] + red_move[0], red[1] + red_move[1])
        
        if maze[blue[0]][blue[1]] != 4:
            d_blue = (blue[0] + blue_move[0], blue[1] + blue_move[1])
    
        if d_red and d_blue:
            if 0 <= d_red[0] < len(maze) and 0 <= d_red[1] < len(maze[0]) and 0 <= d_blue[0] < len(maze) and 0 <= d_blue[1] < len(maze[0]):
                if maze[d_red[0]][d_red[1]] != 5 and maze[d_blue[0]][d_blue[1]] != 5:
                    if not red_visited[d_red[0]][d_red[1]] and not blue_visited[d_blue[0]][d_blue[1]] and not (d_red == d_blue):
                        if not (red == d_blue and blue == d_red):
                            red_visited[d_red[0]][d_red[1]] = True
                            blue_visited[d_blue[0]][d_blue[1]] = True
                            backtracking(maze, d_red, d_blue, count + 1, red_visited, blue_visited)
                            red_visited[d_red[0]][d_red[1]] = False
                            blue_visited[d_blue[0]][d_blue[1]] = False
                        
        if d_red and (d_blue is None):
            if 0 <= d_red[0] < len(maze) and 0 <= d_red[1] < len(maze[0]):
                if maze[d_red[0]][d_red[1]] != 5:
                    if not red_visited[d_red[0]][d_red[1]] and not (d_red == blue):
                        red_visited[d_red[0]][d_red[1]] = True
                        backtracking(maze, d_red, blue, count + 1, red_visited, blue_visited)
                        red_visited[d_red[0]][d_red[1]] = False
                        
        if (d_red is None) and d_blue:
            if 0 <= d_blue[0] < len(maze) and 0 <= d_blue[1] < len(maze[0]):
                if maze[d_blue[0]][d_blue[1]] != 5:
                    if not blue_visited[d_blue[0]][d_blue[1]] and not (d_blue == red):
                        blue_visited[d_blue[0]][d_blue[1]] = True
                        backtracking(maze, red, d_blue, count + 1, red_visited, blue_visited)
                        blue_visited[d_blue[0]][d_blue[1]] = False
            

def solution(maze):
    red = blue = None
    
    red_visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    blue_visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 1:
                red = (r, c)
            elif maze[r][c] == 2:
                blue = (r, c)
    
    red_visited[red[0]][red[1]] = blue_visited[blue[0]][blue[1]] = True
    backtracking(maze, red, blue, 0, red_visited, blue_visited)
    
    return answer if answer != int(1e9) else 0