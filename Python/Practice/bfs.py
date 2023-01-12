# bfs

# 큐를 사용해서 구현한다.
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = False

    while queue:
        v = queue.popleft()
        print(v, end="")

        for i in graph[v]:
            if visited[i]:
                queue.append(i)
                visited[i] = False

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [True] * 9

bfs(graph, 1, visited)