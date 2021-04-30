# 백준1149_RGB거리_DP_실버 1
# 메모리 29028kb, 시간 64ms

import sys

n = int(input())
colors = []
for _ in range(n):
    colors.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,n):
    colors[i][0] += min(colors[i-1][1], colors[i-1][2])
    colors[i][1] += min(colors[i-1][0], colors[i-1][2])
    colors[i][2] += min(colors[i-1][0], colors[i-1][1])
print(min(colors[-1]))
