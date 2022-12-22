# 잘라서 배열로 저장하기
import math


def solution(my_str, n):
    answer = []
    first_index = 0
    count = 1

    for i in range(math.ceil(len(my_str) / n)):
        answer.append(my_str[first_index:n*count])
        first_index = first_index + n
        count += 1
    return answer

print(solution("abc1Addfggg4556b", 6))

"""
0 1 2 3 4 5
6 7 8 9 10 11
12 13 14 16 17

0          n
n          n*2
n+n        n*3
"""
