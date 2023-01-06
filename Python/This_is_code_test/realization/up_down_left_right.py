# 상하좌우

n = int(input())
input_list = list(map(str, input().split()))
x, y = 1, 1

# L -> (0, -1) R -> (0, 1) U -> (1, 0) D -> (-1, 0)
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]
direction_list = ["L", "R", "U", "D"]

for direction in input_list:
    for i in range(len(direction_list)):
        if direction == direction_list[i]:
            mx = x + move_x[i]
            my = y + move_y[i]

    if mx < 1 or my < 1 or mx > n or my > n:
        continue
    x, y = mx, my

print(x, y)