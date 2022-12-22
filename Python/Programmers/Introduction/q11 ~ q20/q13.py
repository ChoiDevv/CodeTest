# 양꼬치

def solution(n, k):
    cnt = k - (n // 10)
    if cnt <= -1:
        cnt = 1
    return 12000 * n + 2000 * cnt