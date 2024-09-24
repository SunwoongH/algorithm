'''
Created by sunwoong on 2024/09/24
'''

def solution(cap, n, deliveries, pickups):
    distance = 0
    delivery = pickup = 0
    
    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            distance += (i + 1) * 2
            delivery -= cap
            pickup -= cap
            
    return distance