'''
Created by sunwoong on 2024/11/20

'''
from collections import defaultdict

def solution(str1, str2):
    sequence_a = defaultdict(int)
    sequence_b = defaultdict(int)
    
    a = set()
    b = set()
    
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            word = str1[i].lower() + str1[i + 1].lower()
            a.add((word, sequence_a[word]))
            sequence_a[word] += 1
            
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            word = str2[i].lower() + str2[i + 1].lower()
            b.add((word, sequence_b[word]))
            sequence_b[word] += 1
    
    intersection = a & b
    union = a | b
    
    if len(union) == 0:
        return 65536
    
    return int(len(intersection) / len(union) * 65536)