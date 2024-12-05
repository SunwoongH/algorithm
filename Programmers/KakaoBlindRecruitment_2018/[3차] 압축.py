'''
Created by sunwoong on 2024/12/05

'''
def solution(msg):
    answer = []
    alpha = list(zip(range(1, 27), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    sequence = 27
    index = dict()
    for num, char in alpha:
        index[char] = num
    
    ban = set()
    for i in range(len(msg)):
        if i in ban:
            continue
        word = msg[i]
        temp = word
        if i == len(msg) - 1:
            answer.append(index[word])
            break
        for k in range(i + 1, len(msg)):
            temp = temp + msg[k]
            if temp not in index:
                index[temp] = sequence
                sequence += 1
                break
            ban.add(k)
            word = temp
        answer.append(index[word])
    
    return answer