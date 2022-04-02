def solution(bridge_length, weight, truck_weights):
    passing = [0 for _ in range(bridge_length)]
    sec = 0
    # while문 1 반복 = 1초
    while passing:
        sec += 1
        passing.pop(0)
        if truck_weights:
            if sum(passing) + truck_weights[0] <= weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)
    return sec

'''
Review
deque로 풀면 테케 중 하나가 시간초과된다
'''