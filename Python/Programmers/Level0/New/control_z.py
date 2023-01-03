# 컨트롤 제트

from collections import deque


def solution(s):
    answer = 0
    stack = deque()
    s = s.split(" ")

    for i in range(len(s)):
        if s[i] != "Z":
            stack.append(s[i])
        else:
            stack.pop()
    
    for num in stack:
        answer += int(num)
    
    return answer

print(solution("10 20 30 40"))