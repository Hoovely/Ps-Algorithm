# 백준_1707_이분 그래프_DFS_골드 4

import sys
input = sys.stdin.readline


def dfs(now):
    for i in range(len(graph[now])):
        next = graph[now][i]
        if color[next] == 0:
            if color[now] == 1:
                color[next] = 2
            elif color[now] == 2:
                color[next] = 1
            dfs(next)


def solution(now):
    global flag
    for i in range(len(graph[now])):
        next = graph[now][i]

        if color[next] == color[now]:
            flag = 1
            return

        if visited[next] == 0:
            visited[next] = 1
            solution(next)

        if flag:
            return


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    color = [0]*(v+1)
    visited = [0]*(v+1)

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v+1):
        if color[i] == 0:
            color[i] = 1
            dfs(i)

    flag = 0
    for i in range(1, v+1):
        if visited[i] == 0:
            visited[i] = 1
            solution(i)

        if flag:
            break

    if flag:
        print("NO")
    else:
        print("YES")
