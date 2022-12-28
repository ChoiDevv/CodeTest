# 삼각형의 완성조건 (1)

def solution(sides):
    sorted_sides = sorted(sides)
    return 2 if sorted_sides[2] >= sorted_sides[0] + sorted_sides[1] else 1

print(solution([1, 2, 3]))