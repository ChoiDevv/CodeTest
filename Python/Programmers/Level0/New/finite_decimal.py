# 유한소수 판별하기

def solution(a, b):
    answer = 0
    b = b // gcd(a, b)

    while b % 2 == 0:
        b = b // 2
    
    while b % 5 == 0:
        b = b // 5
    
    return 1 if b == 1 else 2

def gcd(a, b):
    
    while True:
        if a % b == 0:
            return b
        r = a % b
        a = b
        b = r

print(solution(7, 20))