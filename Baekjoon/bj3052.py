num = []
for i in range(0, 10):
    inputNum = int(input())
    num.append(inputNum)

mod = []
for i in num:
    mod.append(i % 42)

count = 1
for i in range(1, 10):
    check = 0
    for j in range(i - 1, -1, -1):
        if mod[i] == mod[j]:
            check = 1
    if check == 0:
        count += 1
print(count)