'''
Created by sunwoong on 2024/09/11

풀이 시간 - 37분
'''
from itertools import product

def solution(users, emoticons):
    answer = []
    for case in product([10, 20, 30, 40], repeat=len(emoticons)):
        service = 0
        price = 0
        for rate, maximum in users:
            user_price = 0
            for i in range(len(case)):
                if case[i] >= rate:
                    user_price += int(emoticons[i] * ((100 - case[i]) * 0.01))
            if user_price >= maximum:
                service += 1
            else:
                price += user_price
        if not answer:
            answer = [service, price]
        else:
            if answer[0] < service:
                answer = [service, price]
            elif answer[0] == service:
                answer[1] = max(answer[1], price)
    return answer