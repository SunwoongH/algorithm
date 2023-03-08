'''
Created by sunwoong on 2023/03/08

풀이 시간 - 53분
'''

def check(r, c, place, size):
    is_safety = True
    buffer = [None for _ in range(size)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    sides = [(0, 2), (0, 3), (1, 3), (1, 2)]
    k = -1
    side_pos = 0
    for oper in move:
        k += 1
        dr = r + oper[0]
        dc = c + oper[1]
        if k < 4:
            if 0 <= dr < size and 0 <= dc < size:
                if place[dr][dc] == 'P':
                    is_safety = False
                    break
                elif place[dr][dc] == 'O':
                    ddr = dr + oper[0]
                    ddc = dc + oper[1]
                    if 0 <= ddr < size and 0 <= ddc < size and place[ddr][ddc] == 'P':
                        is_safety = False
                        break
                buffer[k] = place[dr][dc]
            continue
        if 0 <= dr < size and 0 <= dc < size and place[dr][dc] == 'P':
            for side in sides[side_pos]:
                if buffer[side] == 'O' or buffer[side] == 'P':
                    is_safety = False
                    break
            if not is_safety:
                break
        side_pos += 1
    return is_safety
                
def solution(places):
    answer = []
    SIZE = 5
    for place in places:
        is_safety = True
        for r in range(SIZE):
            for c in range(SIZE):
                if place[r][c] == 'P':
                    if not check(r, c, place, SIZE):
                        is_safety = False
                        break
            if not is_safety:
                break
        answer.append(1 if is_safety else 0)
    return answer