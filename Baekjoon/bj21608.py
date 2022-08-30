'''
Created by sunwoong on 2022/08/30
'''
import sys
import collections

def allocation_of_seat(student: int):
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    possible = []
    friends = 0
    for r in range(n):
        for c in range(n):
            if not class_room[r][c]:
                friend = 0
                for oper in move:
                    dr = r + oper[0]
                    dc = c + oper[1]
                    if dr >= 0 and dr < n and dc >= 0 and dc < n:
                        if class_room[dr][dc] and class_room[dr][dc] in students[student]:
                            friend += 1
                if friend > friends:
                    friends = friend
                    possible.clear()
                    possible.append((r, c))
                elif friend == friends:
                    possible.append((r, c))
    max_empty = 0
    result = 0
    for i in range(len(possible)):
        empty = 0
        for oper in move:
            dr = possible[i][0] + oper[0]
            dc = possible[i][1] + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < n and not class_room[dr][dc]:
                empty += 1
        if empty > max_empty:
            max_empty = empty
            result = i
    class_room[possible[result][0]][possible[result][1]] = student
    
def satisfaction_survey() -> int:
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    score = {0:0, 1:1, 2:10, 3:100, 4:1000}
    satisfaction = 0
    for r in range(n):
        for c in range(n):
            friend = 0
            for oper in move:
                dr = r + oper[0]
                dc = c + oper[1]
                if dr >= 0 and dr < n and dc >= 0 and dc < n:
                    if class_room[dr][dc] and class_room[dr][dc] in students[class_room[r][c]]:
                        friend += 1
            satisfaction += score[friend]
    return satisfaction

n = int(sys.stdin.readline())
class_room = [[0 for _ in range(n)] for _ in range(n)]
students = collections.defaultdict(list)
order = []
for _ in range(n ** 2):
    student, *like =  map(int, sys.stdin.readline().split())
    students[student].extend(like)
    order.append(student)
for student in order:
    allocation_of_seat(student)
print(satisfaction_survey())