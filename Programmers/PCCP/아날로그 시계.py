'''
Created by sunwoong on 2025/02/03
'''

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start = h1 * 60 * 60 + m1 * 60 + s1
    end = h2 * 60 * 60 + m2 * 60 + s2
    
    if start == 0 or start == 60 * 60 * 12:
        answer += 1
    
    for t in range(start, end):
        ss = (t * 6) % 360
        sm = (t / 10) % 360
        sh = (t / 120) % 360
        
        es = 360 if ((t + 1) * 6) % 360 == 0 else ((t + 1) * 6) % 360
        em = 360 if ((t + 1) / 10) % 360 == 0 else ((t + 1) / 10) % 360
        eh = 360 if ((t + 1) / 120) % 360 == 0 else ((t + 1) / 120) % 360
        
        if ss < sh and eh <= es:
            answer += 1
        if ss < sm and em <= es:
            answer += 1
        if eh == em and eh == es:
            answer -= 1
            
    return answer
    