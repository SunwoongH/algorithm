def checkNum(num):
    temp = list(str(num))
    check = 0
    
    result = True
    if len(temp) == 1:
        pass
    else:
        checkR = int(temp[1]) - int(temp[0])
        for i in range(1, len(temp) - 1):
            check = int(temp[i + 1]) - int(temp[i])
            if check != checkR:
                result = False
                break
    return result
       
inputNum = int(input())
count = 0
for i in range(1, inputNum + 1):
    if checkNum(i):
        count += 1
print(count)