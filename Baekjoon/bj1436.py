'''
문제 - 영화감독 숌

풀이 방법 - 주어진 조건은 6이 적어도 3개 이상 연속으로 들어가는 수를 종말의 숫자로 정의하고 있다.
           해당 조건은 간단하게 in 연산자를 활용하여 검사할 수 있기 때문에 num 값을 순차적으로 증가시키며
           설정한 조건 검사를 통해 n번째 종말의 숫자를 구하는 풀이다.
'''
import sys

n = int(sys.stdin.readline())
num = 666
while True:
    if '666' in str(num): n -= 1
    if n == 0:
        print(num)
        break
    num += 1