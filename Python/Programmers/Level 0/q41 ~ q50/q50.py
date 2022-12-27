# 문자열 정리하기 (2)

def solution(my_string):
    return ''.join(sorted(my_string.lower()))

print(solution("Bcad"))
