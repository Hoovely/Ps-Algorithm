# 백준_14503_로봇 청소기_BFS_골드 5

import sys
input = sys.stdin.readline

def dfs(a,b,d):
    global cnt
    if maps[a+dx[d]][b+dy[d]] == 0:
        cnt += 1
        if d==0:
            dfs(a+dx[d], b+dy[d], 3)
        else:
            dfs(a+dx[d], b+dy[d], abs(1-d))
    else:
        for i in range(4):
            if i == d:
                continue 
            x = a + dx[0]
            y = b + dy[0]

dx = [0,-1,0,1]
dy = [-1,0,1,0]

n,m = map(int,input().split())
r,c,d = map(int,input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int,input().split())))

cnt = 0
dfs(r,c,d)