'''
Created by sunwoong on 2023/02/11

풀이 시간 - 108분
'''
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

def climb_to_the_top(current, tree, cost, costs):
    if current == "center" or not cost:
        return
    next_cost = int(cost * 0.1) if int(cost * 0.1) >= 1 else 0
    costs[current] += cost - next_cost
    climb_to_the_top(tree[current], tree, next_cost, costs)

def solution(enroll, referral, seller, amount):
    tree = defaultdict(str)
    costs = defaultdict(int)
    answer = []
    for i in range(len(enroll)):
        tree[enroll[i]] = referral[i] if referral[i] != '-' else "center"
    for i in range(len(seller)):
        climb_to_the_top(seller[i], tree, amount[i] * 100, costs)
    for i in range(len(enroll)):
        answer.append(costs[enroll[i]])
    return answer