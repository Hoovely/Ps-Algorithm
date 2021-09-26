# 백준_14938_서강그라운드_플로이드-와샬_골드 4

import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m, l = map(int, input().split())
nums = list(map(int, input().split()))
dist = [[INF for _ in range(n)]for _ in range(n)]

for i in range(l):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
                continue
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

min_num = 0
for i in range(n):
    temp = 0
    for j in range(n):
        if dist[i][j] <= m:
            temp += nums[j]
    if min_num < temp:
        min_num = temp

print(min_num)
