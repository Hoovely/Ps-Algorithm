# 백준_2146_다리 만들기_BFS_골드 3

import sys
from collections import deque
input = sys.stdin.readline


def bfs1(cnt):
    while move:
        a, b = move.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if maps[x][y] != 0:
                    if visited[x][y] == 0:
                        visited[x][y] = 1
                        maps[x][y] = cnt
                        move.append([x, y])
                else:
                    edge.append((a, b))


def bfs2(number):
    global min_num
    while move:
        a, b = move.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and visited[x][y] == 0:
                if maps[x][y] == 0:
                    visited[x][y] = 1
                    lenght[x][y] = lenght[a][b] + 1
                    move.append([x, y])

                elif maps[x][y] != number:
                    if lenght[a][b] < min_num:
                        min_num = lenght[a][b]


n = int(input())
maps = []
visited = [[0]*n for _ in range(n)]
lenght = [[0]*n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(n):
    maps.append(list(map(int, input().split())))

cnt = 1
move = deque()
edge = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            maps[i][j] = cnt
            move.append([i, j])
            bfs1(cnt)
            cnt += 1

edge = list(set(edge))
min_num = 1000000
for i in edge:
    visited = [[0]*n for _ in range(n)]
    x, y = i[0], i[1]
    move.append([x, y])
    bfs2(maps[x][y])

print(min_num)
