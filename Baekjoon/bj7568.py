'''
문제 - 덩치

풀이 방법 - 모든 경우의 수를 검사하는 브루트 포스 풀이.
'''
import sys

n = int(sys.stdin.readline())
profile = []
results = []
for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    profile.append((weight, height))
for i in range(len(profile)):
    rank = 1
    for j in range(len(profile)):
        if profile[i][0] < profile[j][0] and profile[i][1] < profile[j][1]:
            rank += 1
    results.append(rank)
print(*results)