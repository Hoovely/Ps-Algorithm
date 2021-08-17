# 백준_17086_아기 상어 2_bfs_실버 2
# 상어의 좌표를 저장하고 빈칸에서 부터 거리를 다 측정하는 방법

import sys
input = sys.stdin.readline


def distance(x, y):
    min_dis = sys.maxsize
    for i in range(len(shark)):
        length = 0
        a = shark[i][0]
        b = shark[i][1]

        dx = abs(x-a)
        dy = abs(y-b)
        while dx != 0 and dy != 0:
            dx -= 1
            dy -= 1
            length += 1

        if min_dis > dx+dy+length:
            min_dis = dx+dy+length

    if min_dis != sys.maxsize:
        return min_dis
    else:
        return 0


n, m = map(int, input().split())

graph = []
shark = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        if lst[j] == 1:
            shark.append([i, j])
    graph.append(lst)

max_dist = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            max_dist = max(max_dist, distance(i, j))
print(max_dist)
