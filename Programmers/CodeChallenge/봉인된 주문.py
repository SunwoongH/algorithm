'''
Created by sunwoong on 2025/06/30
'''
alpha = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j',
        11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s',
        20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

def convert(pos):
    result = []
    
    while pos > 26:
        pos, num = divmod(pos, 26)
        if num == 0:
            pos -= 1
            num = 26
        result.append(alpha[num])
    result.append(alpha[pos])
    result.reverse()
    
    return ''.join(result)

def solution(n, bans):
    bans.sort(key=lambda x: (len(x), x))
    result = convert(n)
    
    for ban in bans:
        if len(ban) < len(result):
            n += 1
            result = convert(n)
        elif len(ban) == len(result) and ban <= result:
            n += 1
            result = convert(n)
    
    return result