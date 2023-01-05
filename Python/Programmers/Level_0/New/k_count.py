# k의 개수

def solution(i, j, k):
    answer = 0
    number_list = list(range(i, j + 1))

    for num in number_list:
        answer += str(num).count(str(k))
    return answer

