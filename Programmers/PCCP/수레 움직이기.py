'''
Created by sunwoong on 2025/02/10
'''

from itertools import product
import sys

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

answer = sys.maxsize

def counting(maze, red_visited, blue_visited, count, red, blue):
    if maze[red[0]][red[1]] == 3 and maze[blue[0]][blue[1]] == 4:
        global answer
        answer = min(answer, count)
        return

    for red_pos, blue_pos in product(move, repeat=2):
        d_red = d_blue = None
        
        if maze[red[0]][red[1]] != 3:
            d_red = (red[0] + red_pos[0], red[1] + red_pos[1])
        if maze[blue[0]][blue[1]] != 4:
            d_blue = (blue[0] + blue_pos[0], blue[1] + blue_pos[1])
        
        if d_red and d_blue:
            if 0 <= d_red[0] < len(maze) and 0 <= d_red[1] < len(maze[0]) and 0 <= d_blue[0] < len(maze) and 0 <= d_blue[1] < len(maze[0]):
                if d_red != d_blue and not red_visited[d_red[0]][d_red[1]] and not blue_visited[d_blue[0]][d_blue[1]]:
                    if maze[d_red[0]][d_red[1]] != 5 and maze[d_blue[0]][d_blue[1]] != 5 and not (d_red == blue and d_blue == red):
                        red_visited[d_red[0]][d_red[1]] = True
                        blue_visited[d_blue[0]][d_blue[1]] = True
                        counting(maze, red_visited, blue_visited, count + 1, d_red, d_blue)
                        red_visited[d_red[0]][d_red[1]] = False
                        blue_visited[d_blue[0]][d_blue[1]] = False
        
        if d_red and (d_blue is None):
            if 0 <= d_red[0] < len(maze) and 0 <= d_red[1] < len(maze[0]):
                if d_red != blue and not red_visited[d_red[0]][d_red[1]]:
                    if maze[d_red[0]][d_red[1]] != 5:
                        red_visited[d_red[0]][d_red[1]] = True
                        counting(maze, red_visited, blue_visited, count + 1, d_red, blue)
                        red_visited[d_red[0]][d_red[1]] = False
                        
        if (d_red is None) and d_blue:
            if 0 <= d_blue[0] < len(maze) and 0 <= d_blue[1] < len(maze[0]):
                if d_blue != red and not blue_visited[d_blue[0]][d_blue[1]]:
                    if maze[d_blue[0]][d_blue[1]] != 5:
                        blue_visited[d_blue[0]][d_blue[1]] = True
                        counting(maze, red_visited, blue_visited, count + 1, red, d_blue)
                        blue_visited[d_blue[0]][d_blue[1]] = False

def solution(maze):
    red = blue = None
    
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 1:
                red = (r, c)
            elif maze[r][c] == 2:
                blue = (r, c)
                
    red_visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    blue_visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    red_visited[red[0]][red[1]] = blue_visited[blue[0]][blue[1]] = True
    counting(maze, red_visited, blue_visited, 0, red, blue)
    
    return answer if answer != sys.maxsize else 0