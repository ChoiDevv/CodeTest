# 다음에 올 숫자

def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * 2

    return answer

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))