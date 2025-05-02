'''
Created by sunwoong on 2025/05/02
'''
import heapq

def solution(program):
    program.sort(key=lambda x: (x[1], x[0]), reverse=True)
    task = program.pop()
    tasks = [((task[0], task[1]), task)]
    answer = [0 for _ in range(11)]
    end = None
    
    while tasks:
        _, task = heapq.heappop(tasks)
        
        if end is None:
            end = task[1] + task[2]
        else:
            if task[1] <= end:
                waiting = end - task[1]
                answer[task[0]] += waiting
                end += task[2]
            else:
                end = task[1] + task[2]
                
        while program and program[-1][1] <= end:
            temp = program.pop()
            heapq.heappush(tasks, ((temp[0], temp[1]), temp))
            
        if not tasks and program:
            temp = program.pop()
            heapq.heappush(tasks, ((temp[0], temp[1]), temp))
            
    answer[0] = end
    return answer