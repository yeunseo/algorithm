from collections import deque

n, m = map(int, input().split())
maze = []

for i in range(n):
    maze.append(list(map(int, input())))

# 동 서 남 북
move_a = [0, 0, 1, -1]
move_b = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()

    # 현재 위치 방문처리
    queue.append((a,b))
    
    while queue:
        a, b = queue.popleft()
        for d in range(4):
            na = a + move_a[d]
            nb = b + move_b[d]
            # 미로를 벗어나는 경우
            if na < 0 or nb < 0 or na >= n or nb >= m:
                continue
            # 괴물이 없고 방문하지 않았던 곳인 경우
            if maze[na][nb] == 1:
                maze[na][nb] = maze[a][b] + 1             
                queue.append((na, nb))                
                
    return maze[n-1][m-1]

print(bfs(0,0))

'''
Review
visited 리스트를 따로 만들 필요가 없었다
새 칸 = 이동 전칸의 값 + 1을 해주면 목적지 칸 까지의 이동 횟수가 나온다는 사실 새로 알았다
'''