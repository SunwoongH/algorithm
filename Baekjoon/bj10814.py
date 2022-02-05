n = int(input())

profile = []
count = 0
for i in range(n):
    age, name = map(str, input().split())
    count += 1
    newData = (count, int(age), name)
    profile.append(newData)

profile.sort(key = lambda x : (x[1], x[0]))

for data in profile:
    print(data[1], data[2])