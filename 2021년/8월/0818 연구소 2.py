# 백준_17141_연구소 2_bfs_골드 5

import sys
import itertools
from collections import deque
import copy
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while move:
        x, y = move.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and check[xx][yy] == 0:
                check[xx][yy] = check[x][y] + 1
                move.append([xx, yy])

    max_second = 0
    flag = 0
    for i in range(n):
        if flag:
            return -1

        max_second = max(max_second, max(check[i]))
        if 0 in check[i]:
            flag = 1

    return max_second


n, m = map(int, input().split())

labs = []
virus = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 2:
            lst[j] = 0
            virus.append([i, j])
        elif lst[j] == 1:
            lst[j] = -1
    labs.append(lst)

virus = deque(itertools.combinations(virus, m))
min_second = sys.maxsize
while virus:
    ab = virus.popleft()
    check = copy.deepcopy(labs)
    move = deque()

    for a, b in ab:
        check[a][b] = 1
        move.append([a, b])

    result = bfs()
    if result != -1:
        min_second = min(min_second, result)

if min_second == sys.maxsize:
    print(-1)
else:
    print(min_second-1)
