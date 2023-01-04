# 저주의 숫자

def solution(n):
    none_three_list = list(filter(lambda x: x % 3 != 0 and "3" not in str(x), [num for num in range(1, 10000)]))
    return none_three_list[n - 1]

print(solution(100))