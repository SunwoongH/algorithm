'''
문제 - 체스판 다시 칠하기

풀이 방법 - 8 x 8 크기로 나뉠 수 있는 모든 경우의 체스판을 확인하면서 각각의 체스판에서 다시 칠해야 하는
           정사각형의 개수를 구하고 최종적으로 모든 경우 중 가장 최소가 되는 개수를 구하는 풀이.
'''
import sys

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip('\n')))

result = sys.maxsize
for i in range(n):
    for j in range(m):
        if i + 7 < n and j + 7 < m:
            odd = 0; even = 0; count = 0
            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if count % 2 == 0:
                        if board[k][l] == 'W': even += 1
                        else: odd += 1
                    else:
                        if board[k][l] == 'B': even += 1
                        else: odd += 1
                    count += 1
                count += 1
            result = min(odd, even, result)
print(result)         