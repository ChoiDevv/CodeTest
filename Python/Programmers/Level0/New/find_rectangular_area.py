# 직사각형 넓이 구하기

def solution(dots):
    print(max(dots)[0])
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots[1]))

print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))