# 제로

import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()

for i in range(n):
    num = int(input())

    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))