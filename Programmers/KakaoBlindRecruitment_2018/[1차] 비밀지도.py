'''
Created by sunwoong on 2024/11/26

'''
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = ""
        
        decoded_arr1 = str(bin(arr1[i])[2:])
        if len(decoded_arr1) < n:
            decoded_arr1 = '0' * (n - len(decoded_arr1)) + decoded_arr1
        
        decoded_arr2 = str(bin(arr2[i])[2:])
        if len(decoded_arr2) < n:
            decoded_arr2 = '0' * (n - len(decoded_arr2)) + decoded_arr2
        
        for j in range(n):
            if decoded_arr1[j] == '0' and decoded_arr2[j] == '0':
                row += ' '
            else:
                row += '#'
                
        answer.append(row)
        
    return answer