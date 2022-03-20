def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer

'''
Review
처음에 itertools permutations 이용했다가 몽땅 시간초과 먹었다
'''