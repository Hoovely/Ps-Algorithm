# 백준_1916_최소비용 구하기_다익스트라_골드 5

import sys
import heapq
input = sys.stdin.readline
INF_num = sys.maxsize

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dist = [INF_num]*(n+1)
dist[start] = 0

heap = []
heapq.heappush(heap, (0, start))
while heap:
    now_cost, now_v = heapq.heappop(heap)

    if dist[now_v] < now_cost:
        continue

    for next_v, next_cost in graph[now_v]:
        if dist[next_v] > now_cost + next_cost:
            dist[next_v] = now_cost + next_cost
            heapq.heappush(heap, (dist[next_v], next_v))

print(dist[end])
