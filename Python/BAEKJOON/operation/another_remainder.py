# 곱셈

from collections import deque

n = int(input())
m = int(input())
answer = n * m

m = deque(str(m))
i = 0

while i < 3:
    print(n * int(m.pop()))
    i += 1

print(answer)