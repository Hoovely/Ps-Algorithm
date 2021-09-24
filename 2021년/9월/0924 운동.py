# 백준_1956_운동_플로이드-와샬_골드 4

import sys
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
city = [[INF for _ in range(v)] for _ in range(v)]
for i in range(e):
    a, b, c = map(int, input().split())
    city[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            city[i][j] = min(city[i][j], city[i][k] + city[k][j])

min_num = INF
for i in range(v):
    if city[i][i] == INF:
        continue
    else:
        min_num = min(min_num, city[i][i])

if min_num == INF:
    print(-1)
else:
    print(min_num)
