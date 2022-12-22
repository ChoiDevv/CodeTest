# 문자열 정렬하기 (1)
import re

def solution(my_string):
    answer = []
    my_string = re.sub('[^0-9]', '', my_string)

    for char in sorted(list(my_string)):
        answer.append(int(char))
    return answer

print(solution("hi12392"))