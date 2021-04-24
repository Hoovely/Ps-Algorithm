# 백준1753_최단경로_다익스트라_골드 5

import sys

def dijkstra(k, a):

    for i in graph[k]:
        for j in i:

    
    

    return min(distance)

def decision(k, a):
    for i in graph:
        for i in j:
            if j[0] == a:
                return dijkstra(k, a)
    return -1

v,e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = [[] for _ in range(v+1)]
move = [[0,0]]
result = []

for i in range(e):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

for i in range(i,v+1):
    if i == k:
        result.append(0)
    else:
        jh = decision(k, i)
        if jh == -1:
            result.append(-1)
        else:
            result.append(jh)
            
