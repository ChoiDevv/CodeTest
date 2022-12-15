# 스택

from collections import deque

def push(stack, number):
    stack.append(number)
    return stack

def pop(stack):
    if not stack:
        return -1
    return stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    if not stack:
        return 1
    return 0

def top(stack):
    if not stack:
        return -1
    return stack[len(stack) - 1]

stack = deque()
count = int(input())

for i in range(count):
    command = input().split()

    if command[0] == "push":
        push(stack, int(command[1]))
    
    if command[0] == "pop":
        print(pop(stack))
    
    if command[0] == "size":
        print(size(stack))
    
    if command[0] == "empty":
        print(empty(stack))
    
    if command[0] == "top":
        print(top(stack))