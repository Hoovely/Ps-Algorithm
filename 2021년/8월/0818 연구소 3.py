# 백준_17142_연구소 3_bfs_골드 4

import sys
import itertools
import copy
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(count):
    while move:
        if count == 0:
            break
        a, b = move.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if check[x][y] == 0:
                    check[x][y] = check[a][b] + 1
                    move.append([x, y])
                    count -= 1
                elif check[x][y] == sys.maxsize:
                    check[x][y] = check[a][b] + 1
                    move.append([x, y])
    max_second = 0
    flag = 0

    for i in range(n):
        for j in range(n):
            if check[i][j] == sys.maxsize:
                continue

            max_second = max(max_second, check[i][j])

        if 0 in check[i]:
            flag = 1

        if flag:
            return -1
    return max_second


n, m = map(int, input().split())

labs = []
virus = []
cnt = 0
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        if lst[j] == 2:
            lst[j] = sys.maxsize
            virus.append([i, j])
        elif lst[j] == 1:
            lst[j] = -1
        elif lst[j] == 0:
            cnt += 1
    labs.append(lst)

virus = deque(itertools.combinations(virus, m))
min_second = sys.maxsize
while virus:
    ab = virus.popleft()
    move = deque()
    check = copy.deepcopy(labs)

    for a, b in ab:
        check[a][b] = 1
        move.append([a, b])

    result = bfs(cnt)
    if result != -1:
        min_second = min(min_second, result)

if min_second == sys.maxsize:
    print(-1)
else:
    print(min_second-1)
