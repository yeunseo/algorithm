answer = 0

# 입력
# n이 세로 m이 가로
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 게임맵 생성
game_map = []
for i in range(n):
    game_map.append(list(input().split()))

# 이동 [북, 동, 남, 서]
move_x = [0, 1, 0, -1]
move_y = [1, 0, -1, 0]

# 방문처리용 맵
visited = [[0]* m for _ in range(n)]
visited[a][b] = 1

def turn_left():
    global d
    d -= 1
    if(d < 0):
        d == 3

while True:
    na = a + move_x[d]
    nb = b + move_y[d]
    if(na)