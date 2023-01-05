# 진료 순서

def solution(emergency):
    answer = [0] * len(emergency)
    idx = 1

    sorted_emergency = sorted(emergency)[::-1]
    
    for num in sorted_emergency:
        answer[emergency.index(num)] = idx
        idx += 1
    
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7]))