'''
Created by sunwoong on 2024/03/20

풀이 시간 - 40분
'''

def solution(friends, gifts):
    # 인덱스 테이블
    index_table = dict()
    for i in range(len(friends)):
        index_table[friends[i]] = i
    # 선물 교환 기록
    record = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for gift in gifts:
        giver, taker = gift.split()
        record[index_table[giver]][index_table[taker]] += 1
    for i in range(len(friends)):
        record[i][i] = -1
    # 선물 지수 테이블
    gift_rate_table = dict()
    for i in range(len(friends)):
        give = 0
        take = 0
        for j in range(len(friends)):
            give += record[i][j]
            take += record[j][i]
        gift_rate_table[friends[i]] = give - take
    # 다음 달 선물 수
    answer = []
    for i in range(len(friends)):
        temp = 0
        for j in range(len(friends)):
            if i == j:
                continue
            if record[i][j] > record[j][i]:
                temp += 1
            elif record[i][j] == record[j][i]:
                if gift_rate_table[friends[i]] > gift_rate_table[friends[j]]:
                    temp += 1
        answer.append(temp)
    return max(answer)
