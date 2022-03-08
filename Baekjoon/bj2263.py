'''
Created by sunwoong on 2022/03/08

>>> 중위 순회와 후위 순회 결과의 특징을 찾아 재귀적으로 분할 정복하여 풀이하였다. 처음 접근하여 풀이했을 때는
시간 초과가 발생했는데 이는 분할을 하기 위한 기준 인덱스인 pivot을 순차 탐색으로 구하는 과정에서 최악의 경우 O(n^2)의
시간 복잡도가 되어 시간 초과가 발생했다고 생각된다. 따라서 pivot을 구하는 과정을 상수 시간으로 최적화하여 해결할 수 있었다.
'''
import sys
sys.setrecursionlimit(10 ** 6)

def preorder(in_left: int, in_right: int, post_left: int, post_right: int) -> None:
    if in_left > in_right or post_left > post_right:
        return
    num = postorder[post_right]
    pivot = index_table[num]
    print(num, end=' ')
    preorder(in_left, pivot - 1, post_left, post_left + (pivot - in_left - 1))
    preorder(pivot + 1, in_right, post_right - (in_right - pivot), post_right - 1)

n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
index_table = {}
for i in range(n):
    index_table[inorder[i]] = i
preorder(0, n - 1, 0, n - 1)