array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    i = 0
    j = 0
    k = 0

    for c in range(len(commands)):
        commands_sliced = commands[c][:3]
        i = commands_sliced[0]-1
        j = commands_sliced[1]
        k = commands_sliced[2]

        sliced = array[i:j]
        sliced.sort()
        answer.append(sliced[k-1])

    return answer


# 더 간단한 방법
def solution2(array, commands):
    answer = []

    for c in commands:
        i, j, k = c
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


print(solution(array, commands))
print(solution2(array, commands))
