# 숫자 찾기

def solution(num, k):
    if str(num).find(str(k)) == -1:
        return -1
    return str(num).find(str(k)) + 1

print(solution(232443, 6))