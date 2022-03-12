'''
Created by sunwoong on 2022/03/12

>>> 주어진 알파벳으로 DFS(깊이 우선 탐색)를 활용해 최소 한 개의 모음과 최소 두 개의 자음으로 구성된 암호를 만드는 풀이
'''
import sys

n, c = map(int, sys.stdin.readline().split())
alphabet = sys.stdin.readline().split()
alphabet.sort()
path = []
results = []
def dfs(i, count_a, count_b):
    if count_a >= 1 and count_b >= 2 and len(path) == n:
        results.append(path[:])
        return
    for j in range(i, len(alphabet)):
        path.append(alphabet[j])
        if alphabet[j] in ['a', 'e', 'i', 'o', 'u']:
            dfs(j + 1, count_a + 1, count_b)
        else:
            dfs(j + 1, count_a, count_b + 1)
        path.pop()
dfs(0, 0, 0)
for result in results:
    print(''.join(result))