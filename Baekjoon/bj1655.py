'''
문제 - 가운데를 말해요

'''
import heapq
import sys

max_left = []
min_right = []
n = int(sys.stdin.readline())
for i in range(1, n + 1):
    num = int(sys.stdin.readline())
    if i == 1:
        heapq.heappush(max_left, (-num, num))
        print(max_left[0][1])
        continue
    
    if max_left[0][1] >= num and not min_right:
        temp = heapq.heappop(max_left)[1]
        heapq.heappush(max_left, (-num, num))
        heapq.heappush(min_right, (temp, temp))  
    elif not min_right or min_right[0][1] < num:
        heapq.heappush(min_right, (num, num))
    else:
        heapq.heappush(max_left, (-num, num))
    
    # 중간값을 구하기 위해 한 쪽으로 num이 몰리는 경우 방지
    if len(max_left) == len(min_right) + 2:
        temp = heapq.heappop(max_left)[1]
        heapq.heappush(min_right, (temp, temp))
    elif len(max_left) + 2 == len(min_right):
        temp = heapq.heappop(min_right)[1]
        heapq.heappush(max_left, (-temp, temp))
    
    # 입력된 num 개수가 짝수, 홀수일때 각각 조건에 맞게 출력
    if i % 2 == 0:
        print(max_left[0][1])
    else:
        if len(max_left) > len(min_right):
            print(max_left[0][1])
        else:
            print(min_right[0][1])