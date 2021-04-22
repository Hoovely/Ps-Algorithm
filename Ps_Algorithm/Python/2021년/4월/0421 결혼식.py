# 백준5567_결혼식_bfs_실버 1

import sys

def bfs():
    while move:
        x = move[0][0]
        y = move[0][1]
        del move
        for i in freind[x]:
            
        




n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
freind = [[] for _ in range(m+1)]
move = [[1,1]]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    freind[a].append(b)
    # freind[b].append(a)

bfs()
    

