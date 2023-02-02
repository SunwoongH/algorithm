'''
Created by sunwoong on 2023/02/02
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(curr):
    if curr in seen:
        return curr, 1
    end, count = None, 0
    seen.add(curr)
    visited[curr] = True
    next = table[curr]
    if not visited[next] or (visited[next] and next in seen):
        end, count = dfs(next)
        seen.remove(curr)
        if end is not None:
            if end in seen:
                count += 1
            else:
                global check
                if not check:
                    global answer
                    check = True
                    answer -= count
    return end, count

t = int(input())
for _ in range(t):
    n = int(input())
    answer = n
    visited = [False for _ in range(n + 1)]
    students = [0] + list(map(int, input().split()))
    table = defaultdict(int)
    for i in range(1, n + 1):
        table[i] = students[i]
    seen = set()
    for i in range(1, n + 1):
        if not visited[i]:
            check = False
            dfs(i)
    print(answer)