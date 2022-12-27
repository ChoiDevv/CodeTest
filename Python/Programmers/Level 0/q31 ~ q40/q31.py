# 옹알이 (1)

def solution(babbling):
    answer = []
    replace = []
    baby_words = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for baby_word in baby_words:
            word = word.replace(baby_word, "#")
        replace.append(word)

    for word in replace:
        word = word.replace("#" ,"")
        answer.append(word)

    return answer.count('')

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))