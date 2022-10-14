'''
Created by sunwoong on 2022/10/14
'''
import sys
import collections

test = int(sys.stdin.readline())
for _ in range(test):
    count_table = collections.defaultdict(int)
    case_1_table = collections.defaultdict(collections.deque)
    case_2_table = collections.defaultdict(collections.deque)
    case_1 = sys.maxsize
    case_2 = -sys.maxsize
    sequence = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())
    for i in range(len(sequence)):
        case_1_table[sequence[i]].append(i)
        case_2_table[sequence[i]].append(i)
        count_table[sequence[i]] += 1
        if count_table[sequence[i]] == k:
            case_1_first = case_1_table[sequence[i]][0]
            case_1_last = case_1_table[sequence[i]][-1]
            case_1 = min(case_1, case_1_last - case_1_first + 1)
            case_1_table[sequence[i]].popleft()
            case_2_first = case_2_table[sequence[i]][0]
            case_2_last = case_2_table[sequence[i]][-1]
            case_2 = max(case_2, case_2_last - case_2_first + 1)
            case_2_table[sequence[i]].popleft()
            count_table[sequence[i]] -= 1
    print(case_1, case_2) if case_1 != sys.maxsize and case_2 != -sys.maxsize else print(-1)