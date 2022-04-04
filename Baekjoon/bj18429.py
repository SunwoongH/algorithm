'''
Created by sunwoong on 2022/04/04
'''
import sys

n, k = map(int, sys.stdin.readline().split())
exercise_kit = list(map(int, sys.stdin.readline().split()))

result, selected_kit = 0, [False] * n
def dfs(before_weight: int, day: int) -> None:
    if day == n + 1 and before_weight >= 500:
        global result
        result += 1
        return
    for i in range(len(exercise_kit)):
        if not selected_kit[i]:
            selected_kit[i] = True
            if before_weight - k + exercise_kit[i] >= 500:
                dfs(before_weight - k + exercise_kit[i], day + 1)
            selected_kit[i] = False
dfs(500, 1)
print(result)