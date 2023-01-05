# 삼각형의 완성조건 (2)

from collections import deque


def solution(sides):
    answer = deque()
    x = 1
    sides = sorted(sides, reverse = True)

    for i in range(sides[0] - sides[1] + 1, sides[0] + 1):
        answer.append(i)
    
    for i in range(sides[0] + 1, sum(sides)):
        answer.append(i)
    
    return len(answer)

print(solution([11, 7]))