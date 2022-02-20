'''
문제 - 2D 행렬 검색 Version 2

m x n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라. 행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다.
'''
from typing import List

# 이진 검색 풀이 - O(mlogn)
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            left, right = 0, len(matrix[row]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if target == matrix[row][mid]:
                    return True
                elif target < matrix[row][mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

# Top-Right 위치에서 시작하여 target이 더 작으면 왼쪽, 크면 아래로 이동하는 검색 풀이 - O(m + n)
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row, column = 0, len(matrix[0]) - 1
        while row <= len(matrix) - 1 and column >= 0:
            if target == matrix[row][column]:
                return True
            elif target < matrix[row][column]:
                column -= 1
            else:
                row += 1
        return False

# 내장 함수 any() 활용 풀이
class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)