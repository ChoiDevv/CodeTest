# 알람 시계

m, n = map(int, input().split())

if n < 45:
    if m == 0:
        m = 24
    m -= 1
    n = (n + 60) - 45
    print(m, n)
else:
    n -= 45
    print(m, n)