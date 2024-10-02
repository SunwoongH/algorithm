'''
Created by sunwoong on 2024/10/02
'''
from collections import defaultdict

def solution(coin, cards):
    max_coin = coin
    check = defaultdict(bool)
    price = defaultdict(int)
    round = 0
    
    mine = cards[:len(cards) // 3]
    for num in mine:
        check[num] = True
        
    for i in range(len(cards) // 3, len(cards) - 1, 2):
        round += 1
        
        price[cards[i]] += 1
        price[cards[i + 1]] += 1

        check[cards[i]] = True
        check[cards[i + 1]] = True
        
        mine.extend([cards[i], cards[i + 1]])
        
        minimum_cost = max_coin + 1
        target = None
        for num in mine:
            cost = price[num]
            if check[len(cards) + 1 - num]:
                cost += price[len(cards) + 1 - num]
                if cost < minimum_cost:
                    minimum_cost = cost
                    target = [num, len(cards) + 1 - num]

        if target:
            if coin >= minimum_cost:
                coin -= minimum_cost
                mine.remove(target[0])
                mine.remove(target[1])
                check[target[0]] = False
                check[target[1]] = False
                if i == len(cards) - 2:
                    round += 1
                continue
        break
        
    return round