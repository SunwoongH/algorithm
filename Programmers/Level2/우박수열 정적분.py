'''
Created by sunwoong on 2022/12/03
'''

def solution(k, ranges):
    area = []
    prev = None
    while k > 1:
        prev = k
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        end = (k - prev) / 2 * pow(len(area) + 1, 2) + (prev - (k - prev) * (len(area))) * (len(area) + 1)
        start = (k - prev) / 2 * pow(len(area), 2) + (prev - (k - prev) * (len(area))) * len(area)
        area.append(end - start)
    for i in range(1, len(area)):
        area[i] += area[i - 1]
    answer = []
    for offset_x, offset_y in ranges:
        x, y = offset_x - 1, len(area) - 1 + offset_y
        if x <= y:
            answer.append((area[y] if y >= 0 else 0) - (area[x] if x >= 0 else 0))
        else:
            answer.append(-1)
    return answer