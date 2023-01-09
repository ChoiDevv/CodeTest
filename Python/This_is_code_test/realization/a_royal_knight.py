# 왕실의 나이트

coordinate = input()
coordinate_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
x, y = coordinate_list.index(coordinate[0]), int(coordinate[1]) - 1
answer = 0

# 우, 좌, 상, 하
dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]

for i in range(8):
    mx = x + dx[i]
    my = y + dy[i]

    if mx < 0 or my < 0 or mx >= 8 or my >= 8:
        continue
    else:
        answer += 1

print(answer)