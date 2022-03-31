from collections import deque

def solution(prices):
    answer = []
    
    queue = deque(prices)
    
    while queue:
        sec = 0
        q = queue.popleft()
        
        for i in queue:
            sec += 1
            if q > i:
                break
        answer.append(sec)
    return answer

'''
Review
스택보다 큐로 푸는게 훨씬 간단했다
break 조건을 안넣었더니 테스트케이스 1번 제외한 모두 실패에 효율성은 죄다 시간초과였다
'''