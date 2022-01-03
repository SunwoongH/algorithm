'''
<로그 파일 재정렬>

로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
'''
from typing import List
from functools import cmp_to_key

class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = sorted(logs, key = cmp_to_key(self.compare))
        return logs
    def compare(self, x: str, y: str) -> int:
        temp1 = x.split()
        temp2 = y.split()
        x_id = temp1[0]
        x = ''.join(temp1[1:])
        y_id = temp2[0]
        y = ''.join(temp2[1:])

        if len(temp1) > len(temp2): max_pos = len(temp2) - 1
        else: max_pos = len(temp1) - 1
        
        if x.isalpha():
            if y.isalpha():
                pos = 1
                while pos <= max_pos:
                    if temp1[pos] == temp2[pos]:
                        pos += 1
                    elif temp1[pos] < temp2[pos]:
                        return -1
                    else:
                        return 1
                if max_pos < len(temp1) - 1: return 1
                elif max_pos < len(temp2) - 1: return -1
                else:
                    if x_id < y_id: return -1
                    elif x_id == y_id: return 0
                    else: return 1
            else: return -1
        else:
            if y.isalpha(): return 1
            else: return 0
            
class Solution2:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits