import sys

x_dict = {}
y_dict = {}
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x not in x_dict:
        x_dict[x] = 1
    else: x_dict[x] += 1
    if y not in y_dict:
        y_dict[y] = 1
    else: y_dict[y] += 1

for key in x_dict.keys():
    if x_dict.get(key) == 1:
        x = key
        break
for key in y_dict.keys():
    if y_dict.get(key) == 1:
        y = key
        break
print(x, y)     