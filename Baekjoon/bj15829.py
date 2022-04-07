'''
Created by sunwoong on 2022/04/07
'''
from typing import List
import sys

length, keys = int(sys.stdin.readline()), list(sys.stdin.readline().rstrip('\n'))

def hash_function(keys: List[str]) -> int:
    hash = 0
    for i, key in enumerate(keys):
        hash += (ord(key) - ord('a') + 1) * 31 ** i
    return hash % 1234567891

print(hash_function(keys))