'''
Created by sunwoong on 2022/12/18
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    i = 0
    time = 0
    count = 0
    bridge_weight = 0
    while i < len(truck_weights):
        time += 1
        if bridge[0] > 0:
            bridge_weight -= bridge[0]
            bridge[0] = 0
            count -= 1
        bridge.rotate(-1)
        if weight - bridge_weight >= truck_weights[i]:
            bridge[-1] = truck_weights[i]
            bridge_weight += truck_weights[i]
            count += 1
            i += 1
    while count > 0:
        time += 1
        if bridge[0] > 0:
            bridge_weight -= bridge[0]
            bridge[0] = 0
            count -= 1
        bridge.rotate(-1)
    return time