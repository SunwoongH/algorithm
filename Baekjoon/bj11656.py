'''
Created by sunwoong on 2022/06/21
'''
word = input().rstrip()
print(*sorted([word[i:] for i in range(len(word))]), sep='\n')