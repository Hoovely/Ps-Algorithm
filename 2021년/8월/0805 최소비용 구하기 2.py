# 백준_1916_최소비용 구하기 2_다익스트라_골드 3

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

dist = [INF]*(n+1)
dist[start] = 0
route = [0]*(n+1)

heap = []
heapq.heappush(heap, (0, start))
while heap:
    now_cost, now_urban = heapq.heappop(heap)

    if dist[now_urban] < now_cost:
        continue

    for next_urban, next_cost in graph[now_urban]:
        if dist[next_urban] > next_cost + now_cost:
            route[next_urban] = now_urban
            dist[next_urban] = next_cost + now_cost
            heapq.heappush(heap, (dist[next_urban], next_urban))

route_v = []
temp = end
while temp:
    route_v.append(temp)
    temp = route[temp]

print(dist[end])
print(len(route_v))
for i in range(len(route_v)-1, -1, -1):
    print(route_v[i], end=" ")
