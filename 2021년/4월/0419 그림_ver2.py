# 백준1926_그림_bfs_실버 1

import sys

def bfs(a,b):
    pic_count = 1

    while move:
        a = move[0][0]
        b = move[0][1]
        del move[0]
        for i in range(4):
            x = a + dn[i]
            y = b + dm[i]
            if 0<=x<n and 0<=y<m and maps[x][y] == 1:
                move.append([x,y])
                maps[x][y] = 0
                pic_count += 1

    return pic_count

n,m = map(int, sys.stdin.readline().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))

dn = [1,-1,0,0]
dm = [0,0,1,-1]

max_pic = 0
count = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            maps[i][j] = 0
            move = [[i,j]]
            max_pic = max(bfs(i,j), max_pic)
            count += 1

print(count)
print(max_pic)
               
