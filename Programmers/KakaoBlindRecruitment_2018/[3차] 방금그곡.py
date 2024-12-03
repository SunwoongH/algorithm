'''
Created by sunwoong on 2024/12/03

'''
def time_to_miniutes(time):
    hour, miniutes = time.split(":")
    return int(hour) * 60 + int(miniutes)

def solution(m, musicinfos):
    answer = None
    
    target = []
    for i in range(len(m)):
        if m[i] == '#':
            target.append(m[i - 1] + m[i])
        elif i == len(m) - 1 or m[i + 1] != '#':
            target.append(m[i])
    
    for musicinfo in musicinfos:
        start, end, music, info = musicinfo.split(",")
        start = time_to_miniutes(start)
        end = time_to_miniutes(end)
        
        time = end - start
        
        new_info = []
        for i in range(len(info)):
            if info[i] == '#':
                new_info.append(info[i - 1] + info[i])
            elif i == len(info) - 1 or info[i + 1] != '#':
                new_info.append(info[i])
        
        count, mod = divmod(time, len(new_info))
        new_info = new_info * count + new_info[:mod]
        
        promising = False
        for i in range(len(new_info) - len(target) + 1):
            is_valid = True
            for k in range(i, i + len(target)):
                if target[k - i] != new_info[k]:
                    is_valid = False
            if is_valid:
                promising = True
                break
        
        if promising:
            if answer is None:
                answer = [music, time]
            else:
                if answer[1] < time:
                    answer = [music, time]
        
    return answer[0] if answer else '(None)'