'''
Created by sunwoong on 2024/03/27

풀이 시간 - 20분
'''
def solution(brown, yellow):
    answer = []
    for num in range(3, 2500):
        if (brown / 2 - num) * (num - 2) == yellow:
            answer.append(num)
    if len(answer) == 1:
        answer.append(answer[-1])
        return answer
    return sorted(answer, reverse=True)