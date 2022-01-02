def checkGroupWord(w):
    temp = {}
    result = True
    preW = ""
    for i in range(len(w)):
        if i != 0:
            if w[i] in temp and preW != w[i]:
                result = False
                break
        temp[w[i]] = True
        preW = w[i]
    return result

n = int(input())
wList = []

for i in range(0, n):
    word = input()
    wList.append(word)

check = 0

for w in wList:
    if checkGroupWord(w):
        check += 1

print(check)