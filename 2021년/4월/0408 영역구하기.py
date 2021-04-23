# 백준2583_영역구하기_dfs_실버 1

import sys
sys.setrecursionlimit(10**6)

def dfs(a,b):
    global n,m,zero_count
    visited[a][b] = 1
    zero_count += 1

    for i in range(4):
        x = a + dn[i]
        y = b + dm[i]
        if 0<=x<n and 0<=y<m and visited[x][y] == 0 and graph[x][y] == 0:
            dfs(x,y)


n,m,k = map(int, sys.stdin.readline().split())
graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dn = [1,-1,0,0]
dm = [0,0,1,-1]
for _ in range(k):
    st_m, st_n, en_m, en_n = map(int,sys.stdin.readline().split())
    for i in range(st_n, en_n):
        for j in range(st_m, en_m):
            graph[i][j] = 1
    
zero = []
count = 0
zero_count = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 0:
            dfs(i,j)
            count += 1
            zero.append(zero_count)
            zero_count = 0

zero.sort()
print(count)
print(*zero)
