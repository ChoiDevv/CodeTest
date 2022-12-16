# 스택 수열

import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque()
check = True
answer = list()
count = 1

for i in range(n):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        count += 1
        answer.append('+')
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        check = False

if check == False:
    print("NO")
else:
    for sym in answer:
        print(sym)
        
"""
첫번째 입력 값 : 4
stack = [1, 2, 3, 4]
현재 count = 4
stack[-1] == 4 -> pop
stack = [1, 2, 3]

두번째 입력 값 : 3
반복문 접근 안함
현재 count = 4
stack[-1] == 3 -> pop
stack = [1, 2]

세번째 입력 값 : 6
stack = [1, 2, 5, 6]
stack[-1] == 6 -> pop
stack = [1, 2, 5]
"""