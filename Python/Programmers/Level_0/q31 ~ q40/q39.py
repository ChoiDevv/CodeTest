# 배열의 유사도

def solution(s1, s2):
    return len([char for char in s1 if char in s2])