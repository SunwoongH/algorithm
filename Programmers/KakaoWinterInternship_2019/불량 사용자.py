'''
Created by sunwoong on 2024/03/29

풀이 시간 - 30분
'''

def check(banned, user):
    is_available = True
    for i in range(len(banned)):
        if banned[i] != user[i] and banned[i] != '*':
            is_available = False
            break
    return is_available

def calculate(available_user, temp, pos, seen):
    if pos >= len(available_user):
        complete_temp = ''.join(sorted(temp))
        if complete_temp not in seen:
            seen.add(complete_temp)
        return
    for available in available_user[pos]:
        if available not in temp:
            temp.append(available)
            calculate(available_user, temp, pos + 1, seen)
            temp.pop()

def solution(user_id, banned_id):
    seen = set()
    available_user = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                is_available = check(banned_id[i], user_id[j])
                if is_available:
                    available_user[i].append(user_id[j])
    calculate(available_user, [], 0, seen)
    return len(seen)