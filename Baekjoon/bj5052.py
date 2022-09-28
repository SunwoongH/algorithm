'''
Created by sunwoong on 2022/09/28
'''
import sys

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    seen = set()
    lengths = set()
    is_consistency = True
    address = []
    for _ in range(n):
        phone = sys.stdin.readline().rstrip()
        address.append(phone)
    address.sort(key=len)
    for phone in address:
        if is_consistency:
            for length in lengths:
                if len(phone) > length and phone[:length] in seen:
                    is_consistency = False
                    break
            seen.add(phone)
            lengths.add(len(phone))
        else:
            break
    print("YES") if is_consistency else print("NO")