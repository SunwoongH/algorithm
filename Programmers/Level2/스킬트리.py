'''
Created by sunwoong on 2024/06/10

풀이 시간 - 15분
'''
def solution(skill, skill_trees):
    seen = set(skill)
    answer = 0
    for data in skill_trees:
        temp = []
        for i in range(len(data)):
            if data[i] in seen:
                temp.append(data[i])
        temp = ''.join(temp)
        if temp == skill[:len(temp)]:
            answer += 1
    return answer