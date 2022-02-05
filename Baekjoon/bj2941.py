croW = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

check = 0
start = 0
while start < len(word):
    tempW = ""
    for w in croW:
        result = word.find(w, start, start + len(w))
        if result != -1:
            tempW = w
            break         
    if tempW != "":
        start += len(tempW)
    else:
        start += 1
    check += 1
print(check)