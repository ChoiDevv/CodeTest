# 피자 나눠 먹기 (3)

def solution(slice, n):
    answer = 0
    return n // slice  if n % slice == 0 else n // slice + 1