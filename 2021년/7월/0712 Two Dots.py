# 백준_16929_Two Dots_DFS_골드 4

import sys
input = sys.stdin.readline

def dfs(now_x,now_y,cnt):
    global start_x, start_y

    if cnt >= 4:
        for i in range(4):
            if now_x + dx[i] == start_x and now_y + dy[i] == start_y:
                print("Yes")
                exit(0)

    for i in range(4):
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]
        if 0<=next_x<n and 0<=next_y<m and visited[next_x][next_y] == 0 and graph[next_x][next_y] == graph[start_x][start_y]:
            visited[next_x][next_y] = 1
            dfs(next_x,next_y,cnt+1)


n,m = map(int,input().split())
graph = []
visited = [[0]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            start_x = i
            start_y = j

            visited = [[0]*m for _ in range(n)]
            visited[i][j] = 1
            dfs(i,j,1)

print("No")