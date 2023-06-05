'''
Created by sunwoong on 2023/06/05
'''
TOP_LIMIT = 5
DOWN_LIMIT = -5

def solution(dirs):
    seen = set()
    move = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    curr_x = curr_y = 0
    answer = 0
    for oper in dirs:
        pivot_x, pivot_y = move[oper]
        next_x, next_y = curr_x + pivot_x, curr_y + pivot_y
        if next_x > TOP_LIMIT or next_x < DOWN_LIMIT or next_y > TOP_LIMIT or next_y < DOWN_LIMIT:
            continue
        front = str(curr_x) + str(curr_y) + str(next_x) + str(next_y)
        back = str(next_x) + str(next_y) + str(curr_x) + str(curr_y)
        if front not in seen and back not in seen:
            answer += 1
            seen.add(front)
            seen.add(back)
        curr_x, curr_y = next_x, next_y
    return answer