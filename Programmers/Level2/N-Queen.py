'''
Created by sunwoong on 2023/03/11
'''

answer = 0
def solution(n):
    visited = [None for _ in range(n)]
    def queen(depth):
        if depth == n:
            global answer
            answer += 1
            return
        for pos in range(n):
            is_promising = True
            for k in range(depth - 1, -1, -1):
                if visited[k] == pos or visited[k] == pos - (depth - k) or visited[k] == pos + (depth - k):
                    is_promising = False
                    break
            if is_promising:
                visited[depth] = pos
                queen(depth + 1)
                visited[depth] = None
    queen(0)
    return answer