n, k = map(int, input().split())
answer = 0
# 1. n에서 1 빼기
# 2. n을 k로 나누기
# n을 1로 만들때까지의 횟수 return
while n != 1:
    if n % k == 0:
        n //= k
        answer += 1
    else:
        n -= 1
        answer +=1

print(answer)