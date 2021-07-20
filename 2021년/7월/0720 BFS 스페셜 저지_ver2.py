# 백준_16940_BFS 스페셜 저지_BFS_골드 4

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

lst = list(map(int, input().split()))
order = [0]*(n+1)
for i in range(n):
    order[lst[i]] = i + 1

for i in range(1, n+1):
    graph[i].sort(key=lambda x: order[x])

visited = [0]*(n+1)
visited[1] = 1
count = 0
move = deque([1])
while move:
    now = move.popleft()
    if now != lst[count]:
        print(0)
        exit(0)

    for i in range(len(graph[now])):
        next = graph[now][i]
        if visited[next] == 0:
            visited[next] = 1
            move.append(next)

    count += 1

print(1)
