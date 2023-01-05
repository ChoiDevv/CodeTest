# 최빈값 구하기

def solution(array):
    answer = 0
    count = 0
    set_list = set(array)

    for num in set_list:
        if array.count(num) == count:
            count = array.count(num)
            answer = -1
        else:
            if array.count(num) > count:
                count = array.count(num)
                answer = num


    return answer

print(solution([1]))