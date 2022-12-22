# 카드2

"""
[1, 2, 3, 4] -> [2, 3, 4] -> [3, 4, 2] -> [4, 2] -> [2, 4] -> [4]
"""

from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque(list(range(1, n + 1)))

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])