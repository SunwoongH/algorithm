'''
Created by sunwoong on 2025/01/16

'''

def insert(word, tree):
    for c in word:
        if c not in tree:
            tree[c] = [dict(), 1]
        else:
            tree[c][1] += 1
        tree = tree[c][0]
        
def find(word, tree):
    for i in range(len(word)):
        if tree[word[i]][1] == 1:
            return i + 1
        tree = tree[word[i]][0]
    return len(word)

def solution(words):
    answer = 0
    tree = dict()
    
    for word in words:
        insert(word, tree)
    
    for word in words:
        answer += find(word, tree)
        
    return answer