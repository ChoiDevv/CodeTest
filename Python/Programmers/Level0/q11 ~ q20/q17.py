# 점의 위치 구하기

def solution(dot):
    answer = 0
    if (dot[0] * dot[1] > 0):
        if (dot[0] > 0):
            answer = 1
        else:
            answer = 3
    else:
        if (dot[0] < 0):
            answer = 2
        else:
            answer = 4
    return answer