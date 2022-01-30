'''
문제 - 일정 재구성

[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘 순(Lexical Order)으로 방문한다.

>>> 상당히 어려웠던 문제였다. 사전 순 DFS를 하면서 출발 여행지를 방문하고 다음 여행지를 방문하는 방식으로 접근해보았지만 풀리지 않았다.
이유는 중간에 경로가 분기하는 경우가 발생하기 때문이였다. 따라서 접근 방식을 달리해야 했고 핵심은 DFS를 통해 목적지를 찾는 것이였다.
가장 처음으로 backtracking이 발생하는 즉, 막다른 길이 목적지가 되고 목적지까지 호출되었던 DFS 함수가 역순으로 backtracking 되면서 최종 경로를 구할 수 있었다. 
'''
from typing import List
import collections

# DFS(재귀) 풀이 - visited를 mark하여 재방문 방지
class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = [{'country' : ticket[1], 'visited' : False}]
            else:
                graph[ticket[0]].append({'country' : ticket[1], 'visited' : False})
        for ticket in graph:
            graph[ticket] = sorted(graph[ticket], key=lambda x : x['country'])
        path = []
        def dfs(country):
            for ticket in graph[country]:
                if not ticket['visited']:
                    ticket['visited'] = True
                    dfs(ticket['country'])
            path.append(country)
        dfs('JFK')
        return path[::-1]

# DFS(재귀) 풀이 - visited를 pop하여 재방문 방지
class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for src, det in sorted(tickets):
            graph[src].append(det)
        path = []
        def dfs(src):
            while graph[src]:
                dfs(graph[src].pop(0))
            path.append(src)
        dfs('JFK')
        return path[::-1]

# DFS(재귀) 풀이 - Solution2에서 O(n) 시간 복잡도를 가지는 pop(0) 연산을 O(1) 시간 복잡도를 가지는 pop() 연산으로 개선
class Solution3:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for src, det in sorted(tickets, reverse=True):
            graph[src].append(det)
        path = []
        def dfs(src):
            while graph[src]:
                dfs(graph[src].pop())
            path.append(src)
        dfs('JFK')
        return path[::-1]

# DFS(반복) 풀이
class Solution4:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for src, det in sorted(tickets, reverse=True):
            graph[src].append(det)
        path = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            path.append(stack.pop())
        return path[::-1]