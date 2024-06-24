'''
Created by sunwoong on 2024/06/24

풀이 시간 - 20분
'''

def solution(number, k):
    temp = []
    for num in number:
        while temp and temp[-1] < num and k > 0:
            k -= 1
            temp.pop()
        temp.append(num)
    return ''.join(temp[:len(temp) - k])