# 백준4963_섬의 개수_dfs_실버 2
# dfs 함수안에서 nh, nw의 범위 제한을 잘못해놔서 고민 30분함;;

import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    visited[x][y] = 1
    
    for i in range(8):
        nh = x + dh[i]
        nw = y + dw[i]
        if 0<=nh<h and 0<=nw<w and maps[nh][nw] == 1 and visited[nh][nw] == 0:
            dfs(nh,nw)

while 1:
    w, h = map(int ,input().split())

    maps = []
    dh = [-1,-1,0,1,1,1,0,-1]
    dw = [0,1,1,1,0,-1,-1,-1]
    visited = [[0]*w for _ in range(h)]
    count = 0

    if w == 0 and h == 0:
        break
    
    for _ in range(h):
        maps.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == 0:
                dfs(i,j)
                count += 1
    
    print(count)

