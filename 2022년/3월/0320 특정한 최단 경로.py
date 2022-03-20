# 백준_특정한 최단 경로_다익스트라_골드 4

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# 다익스트라


def dijkstra(start):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        Now_Dist, Now_Vertex = heapq.heappop(heap)
        if dist[Now_Vertex] < Now_Dist:
            continue
        for Next_Vertex, Next_Dist in graph[Now_Vertex]:
            if Now_Dist + Next_Dist < dist[Next_Vertex]:
                dist[Next_Vertex] = Now_Dist + Next_Dist
                heapq.heappush(heap, (Now_Dist + Next_Dist, Next_Vertex))


n, e = map(int, input().split())
dist = [INF]*801
graph = [[]for _ in range(801)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

dijkstra(1)
d1, d2 = dist[v1], dist[v2]

dist = [INF] * (n+1)
dijkstra(v1)
u, a1 = dist[v2], dist[n]

dist = [INF] * (n+1)
dijkstra(v2)
a2 = dist[n]

result = min(d1+u+a2, d2+u+a1)
if result < INF:
    print(result)
else:
    print(-1)
