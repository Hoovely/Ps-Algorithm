# 백준10026_적록색약_dfs_골드 5

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs_rgb(i, j, color):
    RGB[i][j] = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < n and 0 <= y < n and RGB[x][y] == color:
            dfs_rgb(x, y, color)


def dfs_rb(i, j, color):
    RB[i][j] = 0
    if color == 'R' or color == 'G':
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < n and (RB[x][y] == 'R' or RB[x][y] == 'G'):
                dfs_rb(x, y, color)
    else:
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < n and 0 <= y < n and RB[x][y] == 'B':
                dfs_rb(x, y, color)


n = int(input())
rgb_count = 0
rb_count = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

colors = ['R', 'G', 'B']
RGB = []
RB = []
for i in range(n):
    RGB.append(list(input().strip()))
    RB.append(list(RGB[i]))


for color in colors:
    for i in range(n):
        for j in range(n):
            if RGB[i][j] == color:
                dfs_rgb(i, j, color)
                rgb_count += 1

for color in colors:
    for i in range(n):
        for j in range(n):
            if RB[i][j] == color:
                dfs_rb(i, j, color)
                rb_count += 1

print(rgb_count, rb_count)
