a = 5
b = 24


def solution(a, b):
    answer = ''
    weekDays = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    maxDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    weekDay = (sum(maxDay[:a-1]) + b) % 7
    answer = weekDays[weekDay]
    return answer


solution(a, b)
