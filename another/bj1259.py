while True:
    data = input()
    if int(data) == 0: break
    reverse_data = list(data)
    reverse_data.reverse()
    reverse_data = int(''.join(reverse_data))
    if reverse_data == int(data): print('yes')
    else: print('no')