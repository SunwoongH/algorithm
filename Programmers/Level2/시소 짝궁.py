from collections import Counter

def solution(weights):
    answer = 0
    counting_table = Counter(weights)
    seen = set(counting_table.keys())
    mutiple = [1, 2, 3, 4]
    weights.sort()
    for weight in weights:
        for pivot in mutiple:
            if pivot == 1:
                answer += counting_table[pivot] * (counting_table[pivot] - 1) // 2
            else:
                if weight * pivot in seen:
                    answer += counting_table[pivot] * counting_table[weight * pivot]
    return answer