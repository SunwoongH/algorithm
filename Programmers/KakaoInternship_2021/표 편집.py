'''
Created by sunwoong on 2025/01/22

'''

def solution(n, k, cmd):
    table = [[i - 1, i + 1] for i in range(n)]
    table[0][0] = table[n - 1][1] = None
    answer = ['O' for _ in range(n)]
    
    stack = []
    now = k
    
    for c in cmd:
        if c == 'C':
            prev, next = table[now]
            stack.append(now)
            answer[now] = 'X'
            if prev is None:
                table[next][0] = None
                now = next
                continue
            if next is None:
                table[prev][1] = None
                now = prev
                continue
            now = next
            table[prev][1] = next
            table[next][0] = prev
        elif c == 'Z':
            pos = stack.pop()
            answer[pos] = 'O'
            prev, next = table[pos]
            if prev is not None:
                table[prev][1] = pos
            if next is not None:
                table[next][0] = pos
        else:
            opt, move = c.split()
            if opt == 'U':
                for _ in range(int(move)):
                    prev, next = table[now]
                    now = prev
            else:
                for _ in range(int(move)):
                    prev, next = table[now]
                    now = next
                    
    return ''.join(answer)
         