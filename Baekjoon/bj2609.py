'''
Created by sunwoong on 2022/04/03
'''
a, b = map(int, input().split())
gcd, lcm = lambda a, b: a if b == 0 else gcd(b, a % b), lambda a, b: a * b // gcd(a, b)
print(gcd(a, b), lcm(a, b), sep='\n')