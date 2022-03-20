numbers = [2, 1, 3, 4, 1]
# numbers=[5,0,2,7]


def solution(numbers):
    answer = []
    numbers.sort()

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] in answer:
                pass
            else:
                answer.append(numbers[i] + numbers[j])
                answer.sort()
    return answer


print(solution(numbers))
