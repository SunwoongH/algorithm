n = int(input())

result = []
for i in range(0, n):
    check = list(input())
    result.append(check)

for i in result:
    score = 0
    scoreI = 0
    for j in i:
        if j == 'O':
            scoreI += 1
            score += scoreI
        else:
            scoreI = 0
    print(score)