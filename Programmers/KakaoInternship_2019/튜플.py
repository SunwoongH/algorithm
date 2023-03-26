'''
Created by sunwoong on 2023/03/25

풀이 시간 - 25분
'''

def solution(s):
    temp = None
    num = ""
    sets = []
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            temp = set()
        elif s[i] == '}':
            temp.add(int(num))
            num = ""
            sets.append(temp)
            temp = None
        else:
            if s[i].isdigit():
                num += s[i]
            else:
                if temp is not None:
                    temp.add(int(num))
                    num = ""
    sets.sort(key=lambda x: len(x))
    answer = [list(sets[0])[0]]
    for i in range(1, len(sets)):
        answer.append(list(sets[i].difference(sets[i - 1]))[0])
    return answer