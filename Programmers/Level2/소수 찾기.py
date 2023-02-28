'''
Created by sunwoong on 2023/02/28
'''
from itertools import permutations

def solution(numbers):
    SIZE = 10_000_000
    prime_numbers = [True for _ in range(SIZE)]
    prime_numbers[0] = prime_numbers[1] = False
    for i in range(2, int(SIZE ** 0.5) + 1):
        if prime_numbers[i]:
            j = 2
            while i * j < SIZE:
                prime_numbers[i * j] = False
                j += 1
    numbers = list(numbers)
    seen = set()
    answer = 0
    for count in range(1, len(numbers) + 1):
        for case in permutations(numbers, count):
            number = int(''.join(case))
            if prime_numbers[number] and number not in seen:
                answer += 1
                seen.add(number)
    return answer