'''
Created by sunwoong on 2024/07/30

풀이 시간 - 300분 (풀이 참조)
'''

def solution(a, b, g, s, w, t):
    low, high = 0, 4 * 10 ** 14 - 10 ** 5
    while low <= high:
        time = (low + high) // 2
        max_g = max_s = 0
        total = 0
        for i in range(len(t)):
            count = time // (t[i] * 2)
            if (time % (t[i] * 2) >= t[i]):
                count += 1
            max_g += min(g[i], w[i] * count)
            max_s += min(s[i], w[i] * count)
            total += min(g[i] + s[i], w[i] * count)
        if a <= max_g and b <= max_s and a + b <= total:
            high = time - 1
        else:
            low = time + 1
    return low