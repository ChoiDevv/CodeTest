# 다항식 더하기

import re

def solution(polynomial):
    answer = ""
    x = 0
    y = 0
    polynomial = polynomial.split(" + ")
    
    for word in polynomial:
        if "x" in word:
            if "x" == word:
                word = "1" + word
            x += int(re.sub(r'[^0-9]', '', word))
        else:
            y += int(word)
    
    x = str(x)
    y = str(y)

    if x == "1":
        x = ""

    if y != "0":
        if x == "0":
            answer = y
        else:
            answer = x + "x" + " + " + y
    else:
        answer = x + "x"

    return answer

print(solution("1 + 1"))