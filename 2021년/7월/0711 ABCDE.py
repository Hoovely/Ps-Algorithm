# 백준_13023_ABCDE_DFS_골드 5

import sys
input = sys.stdin.readline


def dfs(idx, cnt):
    global flag
    if cnt == 4:
        flag = 1
        return

    visited[idx] = 1
    for i in range(len(graph[idx])):
        if visited[graph[idx][i]] == 0:
            dfs(graph[idx][i], cnt+1)
            if flag:
                return

    visited[idx] = 0


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0]*n
flag = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n):
    dfs(i, 0)
    print(visited)
    if flag:
        break

print(flag)
