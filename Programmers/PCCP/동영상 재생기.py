'''
Created by sunwoong on 2025/01/28
'''

def calculate_time(video_len, pos, op_start, op_end, command):
    video_miniute, video_second = video_len.split(':')
    video = int(video_miniute) * 60 + int(video_second)
    
    pos_miniute, pos_second = pos.split(':')
    pos = int(pos_miniute) * 60 + int(pos_second)
    
    op_s_miniute, op_s_second = op_start.split(':')
    op_start = int(op_s_miniute) * 60 + int(op_s_second)
    
    op_e_miniute, op_e_second = op_end.split(':')
    op_end = int(op_e_miniute) * 60 + int(op_e_second)
    
    if op_start <= pos <= op_end:
        pos = op_end
    
    if command == 'next':
        pos = min(video, pos + 10)
    else:
        pos = max(0, pos - 10)
        
    if op_start <= pos <= op_end:
        pos = op_end
    
    miniute, second = divmod(pos, 60)
    return f"{miniute:02}:{second:02}"

def solution(video_len, pos, op_start, op_end, commands):
    for command in commands:
        pos = calculate_time(video_len, pos, op_start, op_end, command)
    
    return pos