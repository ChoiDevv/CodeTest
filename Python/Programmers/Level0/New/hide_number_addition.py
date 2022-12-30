# 숨어있는 숫자의 덧셈 (2)

import re

def solution(my_string):
    answer = 0
    my_string_list = list((re.sub("[a-zA-Z]", " ", my_string)).split(" "))

    while '' in my_string_list:
        my_string_list.remove('')

    if len(my_string_list) > 0:
        for word in my_string_list:
            answer += int(word)
    
    return answer

print(solution("1a2b3c4d123Z"))