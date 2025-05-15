'''
Created by sunwoong on 2025/05/15
'''
def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    promising = []
    
    for i in range(row_begin - 1, row_end):
        row = data[i]
        total = 0
        for col in row:
            total += col % (i + 1)
        promising.append(total)
        
    if len(promising) == 1:
        return promising[0]
    
    answer = None
    for i in range(1, len(promising)):
        if answer is None:
            answer = promising[i - 1] ^ promising[i]
        else:
            answer ^= promising[i]
        
    return answer