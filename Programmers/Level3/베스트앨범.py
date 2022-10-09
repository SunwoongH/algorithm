'''
Created by sunwoong on 2022/10/09
'''
from collections import defaultdict

def solution(genres, plays):
    genres_table = defaultdict(list)
    for i, genre in enumerate(genres):
        genres_table[genre].append(i)
    play_table = defaultdict(int)
    for i, play in enumerate(plays):
        play_table[i] += play
    genres = sorted(genres_table.keys(), key=lambda x: -sum(map(lambda y: play_table[y], genres_table[x])))
    answer = []
    for genre in genres:
        answer.extend(sorted(genres_table[genre], key=lambda x: -play_table[x])[:2])
    return answer