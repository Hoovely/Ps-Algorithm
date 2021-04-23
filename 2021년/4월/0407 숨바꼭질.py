# 백준1697_숨바꼭질_bfs_실버 1

from collections import deque
import sys

n,k = map(int,sys.stdin.readline().split())

maps = [0]*100001
dx = [1,-1]
move = deque([n])

while 1:
    a = move.popleft()
    if a == k:
        break

    for i in range(3):
        if i != 2:
            x = a + dx[i]
        else:
            x = 2*a
        if 0<=x<100001 and maps[x] == 0:
            maps[x] = maps[a] + 1
            move.append(x)        

print(maps[a])