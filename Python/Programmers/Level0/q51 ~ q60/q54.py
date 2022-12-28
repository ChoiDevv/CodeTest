# OX퀴즈

def solution(quiz):
    answer = []

    for question in quiz:
        question = question.split()

        if question[1] == "+":
            result = int(question[0]) + int(question[2])
        else:
            result = int(question[0]) - int(question[2])

        if result == int(question[4]):
            answer.append("O")
        else:
            answer.append("X")

    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))