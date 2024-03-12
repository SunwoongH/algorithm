'''
Created by sunwoong on 2024/03/12

풀이 시간 - 40분
'''
from collections import defaultdict

def solution(s):
    s = list(s)
    length_table = defaultdict(int)
    length_table[len(s)] = len(s)
    for i in range(1, len(s) // 2 + 2):
        temp = None
        count = 1
        word = []
        st, ed = 0, i
        while ed <= len(s):
            if not temp:
                temp = s[st:ed]
            else:
                if temp == s[st:ed]:
                    count += 1
                else:
                    if count > 1:
                        word.append(str(count))
                        count = 1
                    word.extend(temp)
                    temp = s[st:ed]
            st, ed = st + i, ed + i
        if count > 1:
            word.append(str(count))
        word.extend(temp)
        if ed - i < len(s):
            word.extend(s[ed - i:])
        length_table[i] = len(''.join(word))
    return min(length_table.values())