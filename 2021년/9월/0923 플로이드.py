# 백준_11404_플로이드_플로이드-와샬_골드 4

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

dist = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[k][j] + dist[i][k])

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF or i == j:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()
