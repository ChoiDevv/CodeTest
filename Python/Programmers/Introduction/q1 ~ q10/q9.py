# 배열의 평균값

def solution(numbers):
    answer = 0
    for number in numbers:
        answer += number
    return answer / len(numbers)