# 백준_11403_최단경로_플로이드-와샬_실버 1

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
graph = []

for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 0:
            lst[j] = INF
    graph.append(lst)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[k][j]+graph[i][k])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()
