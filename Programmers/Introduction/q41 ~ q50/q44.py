# 순서쌍의 개수

def solution(n):
    divide_number = 1
    answer = []

    while True:
        if n % divide_number == 0:
            if (divide_number > n // divide_number):
                return len(answer) * 2
            answer.append((divide_number, n // divide_number))
            if (divide_number == n // divide_number):
                return len(answer) * 2 - 1
        divide_number += 1

print(solution(100))

"""
왼쪽 수를 a, 오른쪽 수를 b라고 가정.
a가 b보다 커지면 리스트를 append한 값의 2배 리턴
a가 b와 같으면 리스트를 append한 값의 2배 - 1 리턴
"""