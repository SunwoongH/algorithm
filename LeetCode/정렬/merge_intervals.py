'''
문제 - 구간 병합

겹치는 구간을 병합하라.
'''
from typing import List

# 정렬 후 병합 풀이 - 투 포인터 방식
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        merged = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                merged.append([start, end])
                start, end = intervals[i][0], intervals[i][1]
            elif end < intervals[i][1]:
                end = intervals[i][1]
        merged.append([start, end])
        return merged

# 정렬 후 병합 풀이 - 값 변경 방식
class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: (x[0], x[1])):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged