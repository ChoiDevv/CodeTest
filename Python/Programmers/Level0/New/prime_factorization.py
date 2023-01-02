# 소인수분해

def solution(n):
    answer = []
    eratosthenes_list = eratosthenes(n)

    for num in eratosthenes_list:
        while n % num == 0:
            answer.append(num)
            n = n // num
    
    if len(answer) == 0:
        answer.append(n)
    
    return list(sorted(set(answer)))

def eratosthenes(num):
    response = [True] * num

    for i in range(2, int(num ** 0.5) + 1):
        if response[i] == True:
            for j in range(i + i, num, i):
                response[j] = False
    
    return [i for i in range(2, num) if response[i] == True]