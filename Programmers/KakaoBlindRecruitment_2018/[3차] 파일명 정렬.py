'''
Created by sunwoong on 2025/01/01

'''
from collections import defaultdict

def solution(files):
    header = defaultdict(str)
    number = defaultdict(int)
    
    new_files = list(zip(range(len(files)), files))
    
    for i, file in enumerate(files):
        start = 0
        switch = True
        for j in range(len(file)):
            if switch:
                if file[j].isdigit():
                    header[i] = file[start:j].lower()
                    start = j
                    switch = False
            else:
                if not file[j].isdigit():
                    number[i] = int(file[start:j])
                    switch = True
                    break
        if not switch:
            number[i] = int(file[start:len(file)])

    new_files.sort(key=lambda x: (header[x[0]], number[x[0]]))

    return list(map(lambda x: x[1], new_files))