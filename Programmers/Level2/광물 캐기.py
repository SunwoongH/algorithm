'''
Created by sunwoong on 2023/04/14
'''
from itertools import permutations

def solution(picks, minerals):
    degree = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    costs = []
    mineral = {'diamond': 0, 'iron': 1, 'stone': 2}
    weapons = []
    for i in range(len(picks)):
        cost = [0 for _ in range(len(minerals))]
        cost[0] = degree[i][mineral[minerals[0]]]
        for j in range(1, len(minerals)):
            cost[j] = degree[i][mineral[minerals[j]]] + cost[j - 1]
        for j in range(picks[i]):
            weapons.append(i)
        costs.append(cost)
    weapons.sort()
    weapons = weapons[:len(weapons) if len(weapons) < 10 else 10]
    answer = None
    for case in permutations(weapons, len(weapons) if len(weapons) < 10 else 10):
        temp = 0
        start, end = None, 4
        for weapon in case:
            if end < len(minerals):
                if start is None:
                    temp += costs[weapon][end]
                else:
                    temp += costs[weapon][end] - costs[weapon][start]
                start, end = end, end + 5
            else:
                temp += costs[weapon][len(minerals) - 1] - costs[weapon][start]
                start = len(minerals) - 1
        if answer is None:
            answer = temp
        else:
            answer = min(answer, temp)
    return answer