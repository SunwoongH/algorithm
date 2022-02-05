def reverseN(value):
    temp = list(value)
    temp.reverse()
    result = int("".join(temp))
    return result

a, b = map(str, input().split())
aN = reverseN(a)
bN = reverseN(b)

if aN > bN:
    print(aN)
else:
    print(bN)