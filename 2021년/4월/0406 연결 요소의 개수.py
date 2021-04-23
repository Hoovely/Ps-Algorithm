# 백준11724_연결 요소의 개수_dfs_실버 2

import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    visited[i] = 1
    for j in graph[i]:
        if visited[j] == 0:
            dfs(j)

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)