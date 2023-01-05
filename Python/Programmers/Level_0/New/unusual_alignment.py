# 특이한 정렬

def solution(num_list, n):
    return list(sorted(num_list, key = lambda num: (abs(num - n), -num)))