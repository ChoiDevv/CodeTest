# 문자 반복 출력하기

def solution(my_string, m):
    answer = ""

    for char in my_string:
        answer += char * m

    return answer

print(solution("hello", 3))