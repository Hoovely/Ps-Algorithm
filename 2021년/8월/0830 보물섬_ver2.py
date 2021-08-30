# 백준_2589_보물섬_BFS_골드 5
# python 3 최적화 버젼

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
        flag = True
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 'L' and visited[xx][yy] == 0:
                visited[xx][yy] = visited[x][y] + 1
                flag = False
                move.append([xx, yy])
        if flag:
            max_num = max(max_num, visited[x][y])

    return max_num


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input().strip()))

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            # 지금 좌표보다 좀 더 멀리있는 좌표가 있을 경우 탐색하지 않는다
            if 1 <= i < n-1 and graph[i-1][j] == 'L' and graph[i+1][j] == 'L':
                continue
            if 1 <= j < m-1 and graph[i][j-1] == 'L' and graph[i][j+1] == 'L':
                continue

            visited = [[0 for _ in range(m)] for _ in range(n)]
            temp = bfs(i, j)
            if temp > result:
                result = temp

print(result-1)
