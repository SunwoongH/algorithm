'''
Created by sunwoong on 2022/04/23
'''
import sys

n, m = map(int, sys.stdin.readline().split())
pokemon_name, pokemon_index = dict(), dict()
for i in range(n):
    pokemon = sys.stdin.readline().rstrip()
    pokemon_name[pokemon] = i + 1
    pokemon_index[i + 1] = pokemon
for _ in range(m):
    data = sys.stdin.readline().rstrip()
    print(pokemon_index[int(data)] if data.isdigit() else pokemon_name[data])