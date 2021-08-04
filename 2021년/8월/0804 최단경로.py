# 백준_1753_최단경로_다익스트라_골드 5

import sys
import heapq
input = sys.stdin.readline
INF_num = sys.maxsize

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [INF_num]*(v+1)
dist[k] = 0

heap = []
heapq.heappush(heap, (0, k))
while heap:
    now_d, now_v = heapq.heappop(heap)

    if dist[now_v] < now_d:
        continue

    for next_v, next_d in graph[now_v]:
        if dist[next_v] > now_d + next_d:
            dist[next_v] = now_d + next_d
            heapq.heappush(heap, (dist[next_v], next_v))

for i in range(1, v+1):
    if dist[i] == INF_num:
        print('INF')
    else:
        print(dist[i])
