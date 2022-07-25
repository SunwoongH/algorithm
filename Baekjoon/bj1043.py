'''
Created by sunwoong on 2022/07/25
'''
import sys

n, m = map(int, sys.stdin.readline().split())
curr_seen = set(map(int, sys.stdin.readline().split()[1:]))
party = dict()
for i in range(m):
    _, *data = list(map(int, sys.stdin.readline().split()))
    party[(frozenset(data), i)] = False
prev_seen = None
while prev_seen != curr_seen:
    temp = set()
    for people in filter(lambda x: not party[x], party.keys()):
        is_seen = False
        for person in people[0]:
            if person in curr_seen:
                is_seen = True
                break
        if is_seen:
            party[people] = True
            temp = temp.union(people[0])
    prev_seen = curr_seen.copy()
    curr_seen = curr_seen.union(temp)
print(m - list(party.values()).count(True))