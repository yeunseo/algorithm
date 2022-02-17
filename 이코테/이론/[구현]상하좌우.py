# 입력
n = int(input())
cmd = input().split()

# 풀이
x = 1
y = 1
move_list = ['L', 'R', 'U', 'D']
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]


for c in cmd:
    for i in range(len(move_list)):
        if c == move_list[i]:
            nx = x + move_x[i]
            ny = y + move_y[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x = nx
    y = ny

print(y, x)

"""
Review

1. 공간의 범위를 벗어날 경우 처리하는 방법에서 조금 막혔다
2. x=nx, y=ny를 통해 이동처리를 해주는걸 for문 밖으로 빼놨었다.
    -> 이러면 continue로 스킵할 수 없다
"""