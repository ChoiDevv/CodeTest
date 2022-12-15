# 문자열 밀기
from collections import deque

def solution(A, B):
    A = deque(A)
    count = 0
    i = 0

    while i < len(list(A)):
        if list(A) == list(B):
            return count

        A.rotate(1)
        count += 1
        i += 1

    if count >= len(list(A)):
        count = -1
    return count

print(solution("hello", "ohell"))