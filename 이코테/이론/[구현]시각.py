n = int(input())

answer = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if('3' in str(h) or '3' in str(m) or '3' in str(s)):
                answer += 1

print(answer)


'''
Review
3이 들어간 시각을
x % 10 == 3 이나 x // 10 == 3 조건을 이용하여 판별하려했었음
이 경우는 중복 카운트되는 경우가 생겨서 귀찮아짐
'''