# 두 수 비교하기

n, m = map(int, input().split())

if n < m:
    print("<")
if n > m:
    print(">")
if n == m:
    print("==")