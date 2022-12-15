# 머쓱이보다 키 큰 사람

def solution(array, height):
    answer = [person for person in array if person > height]
    return len(answer);