'''
문제 - 유효한 괄호

괄호로 된 입력값이 올바른지 판별하라.
'''

class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        check = True
        for token in s:
            if token in '[{(':
                stack.append(token)
            else:
                if not stack:
                    check = False
                    break
                temp = stack.pop()
                if token == ')' and temp != '(':
                    check = False
                elif token == '}' and temp != '{':
                    check = False
                elif token == ']' and temp != '[':
                    check = False
                if not check:
                    break
        if check and stack:
            check = False
        return check

# 매핑 테이블 풀이
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')':'(', '}':'{', ']':'['}
        for token in s:
            if token not in table:
                stack.append(token)
            elif not stack or table[token] != stack.pop():
                return False
        return len(stack) == 0