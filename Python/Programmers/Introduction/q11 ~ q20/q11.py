# 짝수의 합

def solution(n):
    num = 2
    answer = 0
    while num <= n:
        answer += num
        num += 2
    return answer