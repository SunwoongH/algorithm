'''
Created by sunwoong on 2023/03/22
'''

def is_promising(processed_book_time):
    for _, _, used in processed_book_time:
        if not used:
            return True
    return False

def solution(book_time):
    START = 0
    END = 1439
    BREAK = 10
    processed_book_time = []
    for start, end in book_time:
        start = start.split(':')
        start = int(start[0]) * 60 + int(start[1])
        end = end.split(':')
        end = int(end[0]) * 60 + int(end[1])
        processed_book_time.append([start, end, False])
    processed_book_time.sort(key=lambda x: x[0])
    room = 0
    while is_promising(processed_book_time):
        room += 1
        time = 0
        for i in range(len(processed_book_time)):
            start, end = processed_book_time[i][0], processed_book_time[i][1]
            if not processed_book_time[i][2] and time <= start and end <= END:
                time = end + BREAK
                processed_book_time[i][2] = True
            if time >= END:
                break
    return room