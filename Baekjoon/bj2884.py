h, m = map(int, input().split())

m = m - 45
if m < 0:
    m = (m + 60) % 60
    h = (h - 1 + 24) % 24
print(h, m)