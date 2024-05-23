'''
Created by sunwoong on 2024/05/23

풀이 시간 - 40분
'''

def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = list(bin(num)[2:])
        flag = False
        for i in range(len(bin_num) - 1, -1, -1):
            if bin_num[i] == '0':
                bin_num[i] = '1'
                if i != len(bin_num) - 1:
                    bin_num[i + 1] = '0'
                flag = True
                break
        if flag:
            answer.append(int(''.join(bin_num), 2))
        else:
            answer.append(int('10' + ''.join(bin_num[1:]), 2))
    return answer