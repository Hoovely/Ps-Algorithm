# 백준_17086_아기 상어 2_bfs_실버 2

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]


def bfs():
    while shark:
        a, b = shark.popleft()
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if graph[x][y] == 0:
                    graph[x][y] = graph[a][b] + 1
                    shark.append([x, y])


n, m = map(int, input().split())

graph = []
shark = deque()
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 1:
            shark.append([i, j])
    graph.append(lst)

bfs()

max_dist = 0
for i in range(n):
    max_dist = max(max_dist, max(graph[i]))

print(max_dist-1)
