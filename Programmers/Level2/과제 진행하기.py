'''
Created by sunwoong on 2023/04/19
'''

def solution(plans):
    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(':'))
        time = hour * 60 + minute
        plans[i][1] = time
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    temp = []
    answer = []
    ongoing = None
    j = 0
    for i in range(1440):
        if j < len(plans) and plans[j][1] == i:
            if ongoing is not None:
                if ongoing[1] > i:
                    temp.append([ongoing[0], ongoing[1] - i])
                else:
                    answer.append(ongoing[0])
            ongoing = [plans[j][0], plans[j][1] + plans[j][2]]
            j += 1
        elif ongoing:
            if ongoing[1] == i:
                answer.append(ongoing[0])
                if temp:
                    content, during = temp.pop()
                    ongoing = [content, i + during]
                else:
                    ongoing = None
        else:
            if temp:
                content, during = temp.pop()
                ongoing = [content, i + during]
    if ongoing:
        answer.append(ongoing[0])
    while temp:
        content, _ = temp.pop()
        answer.append(content)
    return answer