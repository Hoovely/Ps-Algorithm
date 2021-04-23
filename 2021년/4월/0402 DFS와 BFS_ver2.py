# 백준1260_DFS와 BFS_bfs, dfs_실버 2

from collections import deque

def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    visited[v] = 1
    move = deque()
    move.append(v)
    while move:
        new_v = move.popleft()
        print(new_v, end = ' ')
        for i in range(1,n+1):
            if visited[i] == 0 and graph[new_v][i] == 1:
                visited[i] = 1
                move.append(i)
                
n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(v)
print()
visited = [0]*(n+1)
bfs(v)