# 삼총사

def solution(number):
    answer = 0

    for i in range(len(number) - 2):
        for j in range(i + 1, len(number) - 1):
            for k in range(j + 1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer

print(solution([-3, -2, -1, 0, 1, 2, 3]))

# 0, 1, 2 / 0, 1, 3 / 0, 1, 4 / 0, 2, 3 / 0, 2, 4 / 0, 3, 4
# 1, 2, 3 / 1, 2, 4 / 1, 3, 4
# 2, 3, 4