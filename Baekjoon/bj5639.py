'''
Created by sunwoong on 2022/03/07

>>> 처음 접근했던 방식은 주어진 전위 순회 결과로 이진 검색 트리를 구축한 뒤 후위 순회를 구하는 풀이였다.
하지만 시간 초과가 발생하여 풀이에 실패하였고 전위 순회 결과로 후위 순회를 구할 수 있는 특징을 찾아 재귀적으로
분할 정복하는 방식으로 해결하였다.
'''
import sys
sys.setrecursionlimit(10 ** 6)

def preorder_to_postorder(left: int, right: int) -> None:
    if left > right:
        return
    pivot, check = left, False
    for i in range(left + 1, right + 1):
        if preorder[pivot] < preorder[i]:
            pivot, check = i, True
            break
    if not check:
        pivot = right + 1
    preorder_to_postorder(left + 1, pivot - 1)
    preorder_to_postorder(pivot, right)
    postorder.append(preorder[left])
            
preorder, postorder = [], []
while True:
    try:
        num = int(sys.stdin.readline())
    except:
        break
    preorder.append(num)
preorder_to_postorder(0, len(preorder) - 1)
for num in postorder:
    print(num)