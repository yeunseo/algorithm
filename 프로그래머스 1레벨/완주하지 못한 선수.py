participant = [mislav, stanko, mislav, ana]
completion = [stanko, ana, mislav]


def solution(participant, completion):
    answer = ''
    dict = {}

    for p in participant:
        if p not in dict:
            dict[p] = 0
        if p in dict:
            dict[p] += 1
    for c in completion:
        if c in dict:
            dict[c] -= 1
    for p in participant:
        if dict[p] == 1:
            answer = p

    return answer


print(solution(participant, completion))
