# 백준1149_RGB거리_DP_실버 1
# 오답 1

import sys

input = sys.stdin.readline
n = int(input())
houses = []
for _ in range(n):
    houses.append(list(map(int, input().split())))

for i in range(1,n):
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    houses[i][1] += min(houses[i-1][0], houses[i-1][2])
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])

print(min(houses[-1]))