n = int(input())

score = {}

for i in range(n):
    temp = input().split()
    score[temp[0]] = int(temp[1])

score = sorted(score.items(), key=lambda x : x[1])

for i in score:
    print(i[0], end=' ')


'''
Review
딕셔너리 사용해서 풀었다
딕셔너리는 sorted() 함수 거치면 리스트+튜플로 변하는듯

lambda 처음 써봤다
lambda x : x[1]은
def lambda(x):
    return x[1] 을 의미한다

'''