'''
Created by sunwoong on 2022/11/24
'''
def solution(order):
    j = 0
    sub_container = []
    for i in range(1, len(order) + 1):
        while sub_container and sub_container[-1] == order[j]:
            sub_container.pop()
            j += 1
        if i == order[j]:
            j += 1
        else:
            sub_container.append(i)
    while sub_container and sub_container[-1] == order[j]:
        sub_container.pop()
        j += 1
    return j