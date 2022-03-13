from audioop import reverse


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()    # 배열 a 오름차순
b.sort(reverse=True)    # 배열 b 내림차순

for i in range(k):
    # a의 작은값들이 b의 큰 값보다 작을 때
    if(a[i] < b[i]):
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))