# 외계어 사전

def solution(spell, dic):
    answer = 2
    sorted_spell = ''.join(sorted(spell))

    for word in dic:
        if ''.join(sorted(word)) == sorted_spell:
            answer = 1
            return answer

    return answer

print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))