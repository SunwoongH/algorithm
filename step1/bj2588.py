A = int(input())
B = int(input())

cal1 = A * (B % 10)
cal2 = A * ((B // 10) % 10)
cal3 = A * ((B // 100) % 10)

print(cal1)
print(cal2)
print(cal3)
print(cal1 + 10 * cal2 + 100 * cal3)