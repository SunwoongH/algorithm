'''
Created by sunwoong on 2022/09/30
'''
import collections

def bfs(begin, target, words, length):
    queue = collections.deque([(begin, 0)])
    while queue:
        word, count = queue.popleft()
        if word == target:
            return count
        for i in range(len(word)):
            for char in length[i]:
                if char != word[i]:
                    new_word = word[:i] + char + word[i + 1:]
                    if new_word in words:
                        queue.append((new_word, count + 1))
    return 0
    
def solution(begin, target, words):
    if target not in words:
        return 0
    length = collections.defaultdict(set)
    for word in words:
        for i in range(len(word)):
            length[i].add(word[i])
    return bfs(begin, target, set(words), length)