# 백준14500_RGB거리 2_DP_골드 5

import sys
input = sys.stdin.readline

n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

flag_1 = 0
flag_2 = 0
flag_3 = 0

for i in range(1, n):
    if i == n-1:
        break
    else:
        rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
        rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
        rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])

print(rgb)
