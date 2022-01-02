word = input()

check = {}

for w in word:
    if w.upper() not in check:
        check[w.upper()] = 1
    elif w.upper() in check:
        check[w.upper()] += 1

max = 0
for key in check.keys():
    if max < check.get(key):
        max = check.get(key)

result = []
for key in check.keys():
    if check.get(key) == max:
        result.append(key)

if len(result) == 1:
    print(result[0])
else:
    print('?')
