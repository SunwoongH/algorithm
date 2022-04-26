'''
Created by sunwoong on 2022/04/26
'''
import sys

n, number = int(sys.stdin.readline()), []
for i in range(n + 1):
    if i == 0:
        m = int(sys.stdin.readline())
    else:
        number.append(int(sys.stdin.readline()))
visited, seen, count, path = [False] * len(number), set(), 0, []
def dfs() -> None:
    if len(path) == m:
        target = int(''.join(map(str, path)))
        if target not in seen:
            global count
            seen.add(target)
            count += 1
        return
    for i in range(len(number)):
        if not visited[i]:
            visited[i] = True
            path.append(number[i])
            dfs()
            visited[i] = False
            path.pop()
dfs()
print(count)