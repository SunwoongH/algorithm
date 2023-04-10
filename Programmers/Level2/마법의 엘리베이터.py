'''
Created by sunwoong on 2023/04/10
'''
def solution(storey):
    DOWN, UP = 0, 10
    count = 0
    storey = str(storey)
    while True:
        storey, target = storey[:len(storey) - 1], storey[-1]
        select = DOWN
        target = int(target)
        if abs(target - DOWN) > abs(target - UP):
            select = UP
            count += abs(target - UP)
        elif abs(target - DOWN) == abs(target - UP):
            if storey and int(storey[-1]) >= 5:
                select = UP
            count += abs(target - DOWN)
        else:
            count += abs(target - DOWN)
        storey = str((int(storey) if storey else 0) + (0 if select == DOWN else 1))
        if storey == '0':
            break
    return count