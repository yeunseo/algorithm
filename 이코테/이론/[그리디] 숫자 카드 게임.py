n, m = map(int, input().split())
data=[]
answer = 0
# 풀이
min_list = []

for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
    min_list.append(min(temp))

    # min_list 사용하지 않는 방법
    # answer = max(answer, min(temp))

answer = max(min_list)


print(answer)