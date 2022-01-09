'''
문제 - 중복 문자 제거

중복된 문자를 제외하고 사전식 순서로 나열하라.
'''
import collections

class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                while stack:
                    if stack[-1] > s[i]:
                        if stack[-1] in s[i + 1:] and s[i] not in stack:
                            stack.pop()
                        else:
                            break
                    elif stack[-1] <= s[i]:
                        break
                if s[i] not in stack:
                    stack.append(s[i])
        return ''.join(stack)

# 재귀 풀이
class Solution2:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

# 리스트 풀이
class Solution3:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)

# 스택 풀이
class Solution4:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)