# 괄호

import sys

n = int(sys.stdin.readline())
count = 0

for i in range(n):
    parenthesis = input()

    for char in parenthesis:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count < 0:
            break

    if count == 0:
        print("YES")
    else:
        print("NO")