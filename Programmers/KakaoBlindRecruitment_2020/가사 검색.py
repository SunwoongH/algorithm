'''
Created by sunwoong on 2024/10/11
'''
tries = {}
tries_rev = {}

def add(length, word, storage):
    node = storage[length]
    node['count'] += 1
    for c in word:
        if c not in node:
            node[c] = {'count': 1}
        else:
            node[c]['count'] += 1
        node = node[c]
    
def search(length, word, storage):
    node = storage[length]
    for c in word:
        if c == '?':
            return node['count']
        if c not in node:
            return 0
        node = node[c]
    return node['count'] 

def solution(words, queries):
    answer = []
    
    for i in range(1, 10001):
        tries[i] = {'count': 0}
        tries_rev[i] = {'count': 0}
        
    for word in words:
        add(len(word), word, tries)
        add(len(word), word[::-1], tries_rev)
        
    for q in queries:
        if q[0] == '?':
            answer.append(search(len(q), q[::-1], tries_rev))
        else:
            answer.append(search(len(q), q, tries))
    
    return answer