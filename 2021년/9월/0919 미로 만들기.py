# 백준_2665_미로만들기_BFS_골드 4

import sys
from collections import deque
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    INF = sys.maxsize
    move = deque()
    move.append([0, 0, 0])
    while move:
        a, b, c = move.popleft()

        if a > INF:
            continue

        if b == n-1 and c == n-1:
            INF = min(INF, a)

        for i in range(4):
            x = b + dx[i]
            y = c + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if graph[x][y] == 1:
                    if visited[a][x][y] == 0:
                        visited[a][x][y] = visited[a][b][c] + 1
                        move.append([a, x, y])
                else:
                    if visited[a+1][x][y] == 0:
                        visited[a+1][x][y] = visited[a][b][c]+1
                        move.append([a+1, x, y])

    return INF


n = int(input())
graph = []
for i in range(n):
    lst = list(input().strip())
    for j in range(n):
        if lst[j] == '1':
            lst[j] = 1
        else:
            lst[j] = 0
    graph.append(lst)
visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n+n)]

print(bfs())
