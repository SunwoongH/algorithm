'''
Created by sunwoong on 2024/03/29

풀이 시간 - 27분
'''
from itertools import permutations

def solution(numbers):
    seen = set()
    numbers = sorted(list(numbers), reverse=True)
    prime_numbers = [True for _ in range(int(''.join(numbers)) + 1)]
    prime_numbers[0] = prime_numbers[1] = False
    for i in range(2, int(int(''.join(numbers)) ** 0.5) + 1):
        if prime_numbers[i]:
            for j in range(i * 2, int(''.join(numbers)) + 1, i):
                if prime_numbers[j]:
                    prime_numbers[j] = False
    for i in range(1, len(numbers) + 1):
        for case in permutations(numbers, i):
            case = int(''.join(case))
            if case not in seen and prime_numbers[case]:
                seen.add(case)
    return len(seen)