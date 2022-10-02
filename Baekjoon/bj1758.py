'''
Created by sunwoong on 2022/10/02
'''
import sys

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    person = int(sys.stdin.readline())
    people.append(person)
people.sort(reverse=True)

result = 0
for i in range(len(people)):
    tip = people[i] - (i + 1 - 1)
    if tip > 0:
        result += tip
print(result)