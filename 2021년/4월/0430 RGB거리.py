# 백준1149_RGB거리_DP_실버 1

import sys

n = int(input())
colors = []
for i in range(n):
    colors.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,n):
    for j in range(3):
        colors[i][j] = min(colors[i-1][(j+1)%3] + colors[i][j], colors[i-1][(j+2)%3] + colors[i][j]) 
print(min(colors[-1]))