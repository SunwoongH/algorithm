'''
Created by sunwoong on 2022/10/12
'''
import sys
import collections
from itertools import product

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
number = set(range(10))
if m > 0:
    broken_number = list(map(int, sys.stdin.readline().split()))
    for broken in broken_number:
        number.remove(broken)
    
end = 500000
cases = []
last_check = False
for length in range(1, len(str(n)) + 2):
    for case in product(number, repeat=length):
        if case[0] == 0 and len(case) > 1:
            continue
        if last_check:
            break
        channel = int(''.join(map(str, case)))
        end = max(end, channel)
        if length == len(str(n)) + 1:
            last_check = True
            cases.append((channel, length))
        else:
            cases.append((channel, length))
        
def bfs(cases, start: int = 100):
    queue = collections.deque([(start, 0)])
    case_count = 1
    visited = [False for _ in range(end + 1)]
    visited[start] = True
    while queue:
        channel, count = queue.popleft()
        if count == case_count:
            while cases and cases[0][1] == case_count:
                temp = cases.popleft()
                if not visited[temp[0]]:
                    visited[temp[0]] = True
                    queue.append(temp)
            if cases:
                case_count = cases[0][1]
        if channel == n:
            return count
        elif channel < n:
            if not visited[channel + 1]:
                visited[channel + 1] = True
                queue.append((channel + 1, count + 1))
        else:
            if not visited[channel - 1]:
                visited[channel - 1] = True
                queue.append((channel - 1, count + 1))
print(bfs(collections.deque(cases)))