from itertools import count

answer = 0
n, m = map(int, input().split())
tray = []

for i in range(n):
    temp = list(map(int, input().split()))
    tray.append(temp)

visited = [[0]*m for _ in range(n)]

def dfs(a, b):
    if a <= -1 or a >= n or b <= -1 or b >= m:
        return False

    if visited[a][b] == 0 and tray[a][b] == 0:    
        # 방문처리
        visited[a][b] = 1
        # 상하좌우 이동
        dfs(a-1, b)
        dfs(a+1, b)
        dfs(a, b-1)
        dfs(a, b+1)
        return True

    return False
    

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)

'''
Review
얼릴 수 있는 공간을 어떻게 카운트해야하는지 떠올리기 어려웠다
dfs,bfs 공부를 더 해야할 것 같다
'''