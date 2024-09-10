'''
Created by sunwoong on 2024/09/10

풀이 시간 - 45분
'''

def solution(today, terms, privacies):
    term_table = dict()
    for term in terms:
        key, value = term.split()
        term_table[key] = int(value)
    answer = []
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        year_plus, month_plus = divmod(month + term_table[term], 12)
        if month_plus == 0:
            month_plus = 12
            year_plus -= 1
        if day == 1:
            day = 28
            month_plus -= 1
            if month_plus == 0:
                month_plus = 12
                year_plus -= 1
        else:
            day -= 1
        year += year_plus
        month = month_plus
        
        today_date = int(today.replace('.', ''))
        date = int(''.join([str(year), str(month) if month > 9 else '0' + str(month), str(day) if day > 9 else '0' + str(day)]))
        if date < today_date:
            answer.append(i + 1)
    
    return answer