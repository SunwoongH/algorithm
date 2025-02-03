'''
Created by sunwoong on 2025/02/03
'''

def solution(bandage, health, attacks):
    temp = health
    end = attacks[-1][0]
    
    attack_table = dict()
    for attack in attacks:
        attack_table[attack[0]] = attack[1]
    
    count = 0
    for t in range(end + 1):
        if t in attack_table:
            temp -= attack_table[t]
            if temp <= 0:
                return -1
            count = 1
            continue
        temp = min(health, temp + bandage[1])
        if count == bandage[0]:
            temp = min(health, temp + bandage[2])
            count = 1
            continue
        count += 1     
    
    return temp