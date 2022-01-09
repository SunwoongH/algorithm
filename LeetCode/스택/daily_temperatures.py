'''
문제 - 일일 온도

매일의 화씨 온도 리스트 T를 입력받아서 더 따뜻한 날씨를 위해서는
며칠을 더 기다려야 하는지를 출력하라.
'''
from typing import List

# 브루트 포스 풀이 - 시간 초과
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = []
        for i in range(len(temperatures)):
            day = 0
            check = False
            for j in range(i + 1, len(temperatures)):
                day += 1
                if temperatures[j] > temperatures[i]:
                    check = True
                    days.append(day)
                    break
            if not check:
                days.append(0)
        return days

# 스택 풀이
class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                days[temp] = i - temp
            stack.append(i)
        return days