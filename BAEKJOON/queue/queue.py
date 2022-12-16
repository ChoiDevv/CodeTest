# 큐

from collections import deque
import sys

def push(queue, number):
    queue.append(number)

def pop(queue):
    if not queue:
        return -1
    return queue.popleft()

def size(queue):
    return len(queue)

def empty(queue):
    if not queue:
        return 1
    return 0

def front(queue):
    if not queue:
        return -1
    return queue[0]

def back(queue):
    if not queue:
        return -1
    return queue[-1]

queue = deque()
n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push(queue, command[1])
    if command[0] == 'pop':
        print(pop(queue))
    if command[0] == 'size':
        print(size(queue))
    if command[0] == 'empty':
        print(empty(queue))
    if command[0] == 'front':
        print(front(queue))
    if command[0] == 'back':
        print(back(queue))
    