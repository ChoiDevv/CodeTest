# 숨어있는 숫자의 덧셈 (1)
import re


def solution(my_string):
    answer = 0
    my_string = re.sub('[^0-9]', '', my_string)
    for num in my_string:
        answer += int(num)

    return answer

print(solution("aAb1B2cC34oOp"))