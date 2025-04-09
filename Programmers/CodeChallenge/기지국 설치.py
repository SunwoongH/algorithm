'''
Created by sunwoong on 2025/04/09
'''

def solution(n, stations, w):
    stage = []
    start = 1
    for station in stations:
        end = station - w - 1
        if start <= end:
            stage.append(end - start + 1)
        start = station + w + 1
    if start <= n:
        stage.append(n - start + 1)
        
    need = 0
    for interval in stage:
        if interval % (2 * w + 1) == 0:
            need += interval // (2 * w + 1)
        else:
            need += interval // (2 * w + 1) + 1
    
    return need