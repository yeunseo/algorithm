answer = 1

# 입력
# n이 세로 m이 가로 & a가 세로 b가 가로
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 게임맵 생성
game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

# 이동 [북, 동, 남, 서]
move_a = [-1, 0, 1, 0]
move_b = [0, 1, 0, -1]

# 방문처리용 맵
visited = [[0]* m for _ in range(n)]
visited[a][b] = 1

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 네 방향 모두 갈 수 있는지/없는지 구분하기 위한 변수
turn_time = 0

while True:
    turn_left()
    na = a + move_a[d]
    nb = b + move_b[d]
    # 새로 옮겨갈 위치에 방문한적 없는 경우, 바다가 아닌 경우 방문처리 후 이동
    if visited[na][nb] == 0 and game_map[na][nb] == 0:
        visited[na][nb] = 1
        a = na
        b = nb
        answer += 1
        turn_time = 0
        continue
    
    # 새로 옮겨갈 위치가 방문한 적 있는 칸인 경우 또는 바다인경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        na = a - move_a[d]
        nb = b - move_b[d]
        
        # 뒤가 바다가 아니면 뒤로 가기
        if game_map[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn_time = 0

print(answer)

'''
Review
1. 어렵다
2. turn_time을 추가해야 모든 방향이 갈 수 없을 때를 처리할 수 있다
3. visited[na][nb] == 0 and game_map[na][nb] == 0 판단이 계속 false로 나와서 열심히 로그찍어보면서 삽질했는데
   알고보니 game_map의 요소들을 string으로 집어넣고있었다^^와우
'''