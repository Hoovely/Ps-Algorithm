# 백준_2206_벽 부수고 이동하기_bfs_골드 4

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    move = deque()
    move.append([0, 0, 0])  # flag 0 은 방문하기 전
    while move:
        x, y, z = move.popleft()
        print(x, y, z)
        if x == n-1 and y == m-1:
            return visited[z][x][y]

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and visited[z][xx][yy] == 0:
                if graph[xx][yy] == 0:  # bfs 진행
                    visited[z][xx][yy] = visited[z][x][y] + 1
                    move.append([xx, yy, z])
                elif graph[xx][yy] == 1 and z == 0:
                    for j in range(4):
                        xxx = xx + dx[j]
                        yyy = yy + dy[j]
                        if 0 <= xxx < n and 0 <= yyy < m:
                            if graph[xxx][yyy] == 1:
                                continue
                            if visited[1][xxx][yyy] == 0:
                                visited[1][xxx][yyy] = visited[0][x][y] + 2
                                move.append([xxx, yyy, 1])
    return -1


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0]*m for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1

print(bfs())
print(visited[1])
