# 이진수 더하기

def solution(bin1, bin2):
    answer = ""
    sum = trans(bin1) + trans(bin2)

    while True:
        answer += str(sum % 2)
        sum = sum // 2

        if sum == 0:
            break

    return answer[::-1]

def trans(bin):
    sum = 0
    bin = bin[::-1]

    for i in range(len(bin)):
        sum += int(bin[i]) * (2 ** i)

    return sum

print(solution("1001", "1111"))