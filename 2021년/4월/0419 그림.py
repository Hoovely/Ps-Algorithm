# 백준1926_그림_dfs_실버 1

import sys
sys.setrecursionlimit(10**6)

def dfs(a,b):
    global picture_count

    for i in range(4):
        x = a + dn[i]
        y = b + dm[i]
        if 0<=x<n and 0<=y<m and maps[x][y] == 1:
            maps[x][y] = 0
            picture_count += 1
            dfs(x,y)

n,m = map(int, sys.stdin.readline().split())
maps = []

dn = [1,-1,0,0]
dm = [0,0,1,-1]

max_pic = 0
picture_count = 0
count = 0

for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            count += 1
            picture_count = 1
            maps[i][j] = 0
            dfs(i,j)
            max_pic = max(picture_count, max_pic)
            
print(count)
print(max_pic)