'''
Created by sunwoong on 2025/04/10
'''

from collections import Counter, defaultdict

def solution(a):
    if len(a) == 1:
        return 0
    if len(a) == 2:
        if a[0] != a[1]:
            return 2
        else:
            return 0
    answer = 0
    compaction = [a[0], a[1]]
    for i in range(2, len(a)):
        if a[i - 2] == a[i - 1] and a[i - 1] == a[i]:
            continue
        compaction.append(a[i])
    
    counting = Counter(compaction)
    maximum = max(counting.values())
    nums = [item[0] for item in counting.items() if item[1] == maximum]
    seen = set(nums)
    nums_index = defaultdict(list)
    for i in range(len(compaction)):
        if compaction[i] in seen:
            nums_index[compaction[i]].append(i)
    for num in nums:
        visited = [False for _ in range(len(compaction))]
        length = 0
        for i in nums_index[num]:
            visited[i] = True
            if i - 1 >= 0 and not visited[i - 1]:
                visited[i - 1] = True
                length += 2
                continue
            if i + 1 < len(compaction) and not visited[i + 1] and compaction[i + 1] != num:
                visited[i + 1] = True
                length += 2
        answer = max(answer, length)
    return answer
        