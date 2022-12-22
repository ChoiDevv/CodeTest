# 개미 군단

def solution(hp):
    ant_attack = [5, 3, 1]
    answer = 0

    for attack in ant_attack:
        if hp < 0:
            return answer
        answer += (hp // attack)
        hp = hp % attack

    return answer

print(solution(999))

"""
장군 개미는 5
병정 개미는 3
일개미는 1

먼저 hp에서 장군개미를 나누고 나온 몫을 answer에 더한다.
나머지 값을 병정 개미로 나누고 나온 몫을 answer에 더한다.
나머지 값을 일개미로 나누고 나온 몫을 answer에 더한다.
"""