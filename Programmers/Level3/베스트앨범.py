'''
Created by sunwoong on 2024/04/30

풀이 시간 - 24분
'''
from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_table = defaultdict(list)
    genre_sum = defaultdict(int)
    for i in range(len(genres)):
        genre_table[genres[i]].append(i)
        genre_sum[genres[i]] += plays[i]
    genre_keys = list(genre_table.keys())
    genre_keys.sort(key=lambda x: -genre_sum[x])
    for genre in genre_keys:
        if len(genre_table[genre]) == 1:
            answer.append(genre_table[genre][0])
            continue
        genre_table[genre].sort(key=lambda x: -plays[x])
        answer.extend(genre_table[genre][:2])
    return answer