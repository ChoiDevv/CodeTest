# 모음 제거

def solution(my_string):
    answer = ""
    for char in my_string:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
            answer += char

    return answer

print(solution("bus"))