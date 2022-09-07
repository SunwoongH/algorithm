'''
Created by sunwoong on 2022/09/07
'''
import sys

board = sys.stdin.readline().rstrip()
new_board = ""

def replace(count: int):
    if count % 2 != 0:
        global is_possible
        is_possible = False
        return
    output = ""
    output += "AAAA" * (count // 4)
    count %= 4
    output += "BB" * (count // 2)
    return output

count = 0
is_possible = True
for i in range(len(board)):
    if board[i] == ".":
        new_string = replace(count)
        if new_string is None:
            break
        else:
            new_board += new_string
        count = 0
        new_board += "."
    else:
        count += 1
new_string = replace(count)
if new_string:
    new_board += new_string

if is_possible:
    print(new_board)
else:
    print(-1)