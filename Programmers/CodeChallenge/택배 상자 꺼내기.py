'''
Created by sunwoong on 2025/03/02
'''

def solution(n, w, num):
    sequence = 1
    box = []
    floor, count = divmod(n, w)
    for i in range(floor):
        nums = list(range(sequence, sequence + w))
        if i % 2 != 0:
            nums.reverse()
        box.append(nums)
        sequence += w
    if count > 0:
        nums = list(range(sequence, sequence + count)) + [0 for _ in range(w - count)]
        if floor % 2 != 0:
            nums.reverse()
        box.append(nums)
    box.reverse()
    
    for c in range(w):
        depth = 0
        for r in range(floor if count == 0 else floor + 1):
            if box[r][c] != 0:
                depth += 1
            if box[r][c] == num:
                return depth