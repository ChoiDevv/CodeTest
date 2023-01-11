# 게임 개발

m, n = map(int, input().split())
x, y, direction = map(int, input().split())
input_map = []
visited_node = [[0] * n for _ in range(n)]

for _ in range(m):
    input_map.append(list(map(int, input().split())))

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited_node[x][y] = 1
count = 1
visited_time = 0

while True:
    direction -= 1
    if direction < 0:
        direction = 3

    mx = x + dx[direction]
    my = y + dy[direction]

    if input_map[mx][my] == 0 and visited_node[mx][my] == 0:
        count += 1
        visited_node[mx][my] = 1
        x, y = mx, my
        visited_time = 0
        continue
    else:
        visited_time += 1

    if visited_time == 4:
        mx = x - dx[direction]
        my = y - dy[direction]

        if visited_node[mx][my] == 0:
            x, y = mx, my
        else:
            break
        visited_time = 0

print(count)