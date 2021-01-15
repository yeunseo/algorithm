answers = [1, 2, 3, 4, 5]
# answers = [1,3,2,4,2]


def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(answers)):
        if answers[i] == student1[i % len(student1)]:
            count1 += 1
        if answers[i] == student2[i % len(student2)]:
            count2 += 1
        if answers[i] == student3[i % len(student3)]:
            count3 += 1

    answer_count = [count1, count2, count3]

    for student, score in enumerate(answer_count, 1):
        if score == max(answer_count):
            answer.append(student)

    return answer


print(solution(answers))
