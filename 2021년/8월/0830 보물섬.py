# 백준_2589_보물섬_BFS_골드 5
# python3 시간초과, pypy 제출

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(a, b):
    visited[a][b] = 1
    move = deque()
    move.append([a, b])
    max_num = 0
    while move:
        x, y = move.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 'L' and visited[xx][yy] == 0:
                visited[xx][yy] = visited[x][y] + 1
                if visited[xx][yy] > max_num:
                    max_num = visited[xx][yy]
                move.append([xx, yy])

    return max_num


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input().strip()))

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0 for _ in range(m)] for _ in range(n)]
            temp = bfs(i, j)
            if temp > result:
                result = temp

print(result-1)
