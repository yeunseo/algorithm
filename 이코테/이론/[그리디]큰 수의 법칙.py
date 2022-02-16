# 큰 수의 법칙

# 입력 (n배열의 크기, m더해지는 횟수, k번을 초과하여 더해질 수 없음)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 풀이
answer = 0
data.sort(reverse=True)

while True:
    for i in range(k):
        if m == 0:
            break
        answer += data[0]
        m -= 1
    if m == 0:
        break
    answer += data[1]
    m -= 1
        
print(answer)

# Review
# while True로 반복해주는 부분을 생각 못했었다.