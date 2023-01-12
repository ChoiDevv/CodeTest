# dfs

# 재귀와 스택을 활용해서 dfs를 구현한다.

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end="")

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * 9
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

dfs(graph, 1, visited)