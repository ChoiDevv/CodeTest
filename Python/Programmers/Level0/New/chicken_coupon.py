# 치킨 쿠폰

def solution(chicken):
    answer = 0
    while chicken >= 10:
        answer += (chicken // 10)
        chicken = (chicken // 10) + (chicken % 10)

    return answer

print(solution(100))