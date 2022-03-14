'''
Created by sunwoong on 2022/03/14
'''
import sys

n = int(sys.stdin.readline())
ability_table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = sys.maxsize
start_team, link_team = [], []
def dfs(r: int, count: int) -> None:
    if count == n // 2:
        global result
        start = link = 0
        for i in range(n):
            if i not in start_team:
                link_team.append(i)
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                start += ability_table[start_team[i]][start_team[j]] + ability_table[start_team[j]][start_team[i]]
                link += ability_table[link_team[i]][link_team[j]] + ability_table[link_team[j]][link_team[i]]
        result = min(result, abs(start - link))
        link_team.clear()
        return
    for c in range(r, n):
        start_team.append(c)
        dfs(c + 1, count + 1)
        start_team.pop()
dfs(0, 0)
print(result)