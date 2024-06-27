'''
Created by sunwoong on 2024/06/27

풀이 시간 - 75분
'''
def convertTo(k, target):
    temp = []
    while target:
        target, mod = divmod(target, k)
        temp.append(str(mod))
    return ''.join(temp[::-1])

def is_prime(target):
    if target == 1:
        return False
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            return False
    return True

def solution(n, k):
    if n == 1:
        return 0
    temp = convertTo(k, n)
    temp = temp.replace('0', ' ')
    promising = temp.split()
    return sum(map(lambda x: is_prime(int(x)), promising))