'''
Created by sunwoong on 2023/02/14
'''
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
big, small = nums[0], nums[1]
big_count = (m // (k + 1)) * k + (m % (k + 1))
total = big * big_count + small * (m - big_count)
print(total)