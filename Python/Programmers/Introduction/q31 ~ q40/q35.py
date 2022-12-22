# 배열 두 배 만들기

from collections import deque

def solution(numbers):
    answer = []
    numbers = deque(numbers)

    while len(numbers) != 0:
        answer.append(numbers.popleft() * 2)

    return answer

print(solution([1, 2, 3, 4, 5]))