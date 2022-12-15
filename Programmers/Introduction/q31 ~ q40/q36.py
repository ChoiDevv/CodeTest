# 연속된 수의 합

def solution(num, total):
    answer = []
    criteria_number = total // num  # 4
    average_number = criteria_number * 2
    answer.append(criteria_number)

    if num % 2 == 0:
        answer.append(criteria_number + 1)
        average_number = (criteria_number + criteria_number + 1)

    while len(answer) != num:
        criteria_number = minus(criteria_number)
        answer.append(criteria_number)
        answer.append(average_number - criteria_number)

    return sorted(answer)


def minus(number):
    number -= 1
    return number


print(solution(4, 14))
