'''
Created by sunwoong on 2024/06/30

풀이 시간 - 60분
'''
def calculate_score(info, path):
    apich = 0
    lian = 0
    for i in range(len(info)):
        if info[i] < path[i]:
            lian += 10 - i
        elif info[i]:
            apich += 10 - i
    return lian - apich

def make_a_path(n, info, pos, path, answer):
    if pos == len(info) - 1:
        path.append(n)
        score = calculate_score(info, path)
        if score > 0:
            answer.append([path[:], score])
        path.pop()
        return
    if info[pos] < n:
        path.append(info[pos] + 1)
        make_a_path(n - info[pos] - 1, info, pos + 1, path, answer)
        path.pop()
    path.append(0)
    make_a_path(n, info, pos + 1, path, answer)
    path.pop()

def solution(n, info):
    answer = []
    make_a_path(n, info, 0, [], answer)
    if not answer:
        return [-1]
    answer.sort(key=lambda x: -x[1])
    maximum = answer[0][1]
    promising = []
    for i in range(len(answer)):
        if answer[i][1] == maximum:
            promising.append(answer[i][0])
            continue
        break
    promising.sort(key=lambda x: ''.join(map(str, x[::-1])), reverse=True)
    return promising[0]