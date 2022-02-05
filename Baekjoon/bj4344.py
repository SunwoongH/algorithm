c = int(input())

cases = []
for i in range(0, c):
    case = list(map(int, input().split()))
    cases.append(case)

for case in cases:
    n = case[0]
    avg = 0
    for num in range(1, len(case)):
        avg += case[num]
    avg /= n
    student = 0
    for num in range(1, len(case)):
        if case[num] > avg:
            student += 1
    percentage = (student / n) * 100
    print('%.3f%%' % percentage)