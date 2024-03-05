'''
Created by sunwoong on 2024/03/05

풀이 시간 - 37분
'''
move = [[(-1, 0), [(-1, 0), (0, -1), (0, 1)]],
        [(0, 1), [(0, 1), (-1, 0), (1, 0)]],
        [(1, 0), [(1, 0), (0, -1), (0, 1)]],
        [(0, -1), [(0, -1), (-1, 0), (1, 0)]]]

def solution(places):
    answer = []
    for place in places:
        is_correct = 1
        p_pos = []
        for r in range(len(place)):
            for c in range(len(place[0])):
                if place[r][c] == 'P':
                    p_pos.append((r, c))
        for r, c in p_pos:
            for oper in move:
                dr = r + oper[0][0]
                dc = c + oper[0][1]
                if 0 <= dr < len(place) and 0 <= dc < len(place[0]):
                    if place[dr][dc] == 'O':
                        for next_oper in oper[1]:
                            ddr = dr + next_oper[0]
                            ddc = dc + next_oper[1]
                            if 0 <= ddr < len(place) and 0 <= ddc < len(place[0]) and place[ddr][ddc] == 'P':
                                is_correct = 0
                                break
                    elif place[dr][dc] == 'P':
                        is_correct = 0
                    if not is_correct:
                        break
            if not is_correct:
                break
        answer.append(is_correct)
    return answer