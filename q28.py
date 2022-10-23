# 짝수 홀수 개수

def solution(num_list):
    answer = [num for num in num_list if num % 2 == 0]
    return [len(answer), len(num_list) - len(answer)]